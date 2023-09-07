# https://zenodo.org/record/2620293#.YkWyDH9Bzmg

import os
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from PIL import Image
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    mkdir,
    remove_dir,
)


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "CODEBRIM"
    dataset_path = "/mnt/d/datasetninja-raw/codebrim/original_dataset"
    images_folder = "images"
    bboxes_folder = "annotations"
    bboxes_ext = ".xml"
    ds_name = "ds"
    batch_size = 10

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        file_name = get_file_name(image_path)

        ann_path = os.path.join(bboxes_path, file_name + bboxes_ext)

        if file_exists(ann_path):
            tree = ET.parse(ann_path)
            root = tree.getroot()

            objects = root.findall(".//object")
            for curr_obj in objects:
                curr_coord = curr_obj.find(".//bndbox")
                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class)
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("defect", sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    images_path = os.path.join(dataset_path, images_folder)
    bboxes_path = os.path.join(dataset_path, bboxes_folder)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = [im_name for im_name in os.listdir(images_path)]

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [os.path.join(images_path, im_name) for im_name in images_names_batch]

        # TODO =========================== must have, check EXIF Rotate 180 =========================
        temp_img_pathes_batch = []
        temp_folder = os.path.join(dataset_path, "temp")
        mkdir(temp_folder)
        for im_path in img_pathes_batch:
            temp_img = cv2.imread(
                im_path,
                flags=cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH | cv2.IMREAD_IGNORE_ORIENTATION,
            )
            new_img_path = os.path.join(temp_folder, get_file_name_with_ext(im_path))
            temp_img_pathes_batch.append(new_img_path)
            cv2.imwrite(new_img_path, temp_img)

        # TODO =======================================================================================

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, temp_img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in temp_img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        remove_dir(temp_folder)

        progress.iters_done_report(len(images_names_batch))
    return project
