from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "CODEBRIM"
PROJECT_NAME_FULL: str = "CODEBRIM: COncrete DEfect BRidge IMage Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    url="https://zenodo.org/record/2620293/files/license.md?download=1", redistributable=False
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Construction()]
CATEGORY: Category = Category.Construction()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2019-04-01"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/2620293#.YkWyDH9Bzmg"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 3292511
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/codebrim"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "CODEBRIM_classification_balanced_dataset.zip": "https://zenodo.org/record/2620293/files/CODEBRIM_classification_balanced_dataset.zip?download=1",
    "CODEBRIM_classification_dataset.zip": "https://zenodo.org/record/2620293/files/CODEBRIM_classification_dataset.zip?download=1",
    "CODEBRIM_cropped_dataset.zip": "https://zenodo.org/record/2620293/files/CODEBRIM_cropped_dataset.zip?download=1",
    "CODEBRIM_original_images.zip": "https://zenodo.org/record/2620293/files/CODEBRIM_original_images.zip?download=1",
    "license.md": "license.md",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "crack": [230, 25, 75],
    "spallation": [60, 180, 75],
    "efflorescence": [255, 225, 25],
    "exposed bars": [0, 130, 200],
    "corrosion stain": [245, 130, 48],
    "background": [145, 30, 180],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/abs/1904.08486"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[
    Union[str, List[str], Dict[str, str]]
] = "https://github.com/ccc-frankfurt/meta-learning-CODEBRIM"

CITATION_URL: Optional[str] = "https://zenodo.org/record/2620293/export/hx"
AUTHORS: Optional[List[str]] = [
    "Martin Mundt",
    "Sagnik Majumder",
    "Sreenivas Murali",
    "Panagiotis Panetsos",
    "Visvanathan Ramesh",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Goethe University, Germany",
    "Egnatia Odos A. E., Greece",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.goethe-university-frankfurt.de/",
    "https://www.egnatia.eu/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Additionally, bounding boxes with 2 or more classes are marked as ***duplicate bbox***. Run dataset in supervisely to explore"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
