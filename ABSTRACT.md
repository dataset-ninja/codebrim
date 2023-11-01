The **CODEBRIM: COncrete DEfect BRidge IMage Dataset** is designed for multi-target classification of five commonly occurring concrete defects. The dataset aims to facilitate the development of robust computer vision techniques tailored to real-world scenarios. In the pursuit of recognizing defects in concrete infrastructure, particularly in bridges, the authors of the dataset acknowledge the inherent challenges in this critical initial step for assessing structural integrity. Concrete materials exhibit significant variations in appearance, influenced by factors such as lighting conditions, weather, and diverse surface characteristics. Additionally, concrete defects often overlap, compounding the complexity of the task.

Recognizing the importance of accurately identifying various defect types concurrently, the authors emphasize the severity of overlapping defects with structural safety assessment. Concrete surfaces' visual properties, including reflectance, roughness, and colour, vary significantly. Addressing these variations necessitates the development of computer vision methods capable of handling such complex visual environments.

The authors' work focuses on two pivotal aspects of concrete defect recognition: the creation of a labeled multi-target dataset with overlapping defect categories and the design of specialized deep neural networks for multi-class multi-target defect classification. The CODEBRIM dataset encompasses six mutually exclusive classes: *crack*, *spallation*, *exposed reinforcement bar*, *efflorescence* (calcium leaching), *corrosion stains*, and non-defective *background*. The dataset comprises high-resolution images captured under varying environmental conditions, including wet or stained surfaces, and features diverse bridges with different deterioration levels and surface appearances.

<img src="https://github.com/supervisely/supervisely/assets/78355358/4a5eb4f6-e84f-4b18-ac6b-0ad818b3f904" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">(a) Top row from left to right: 1) exposed bars, spallation, cracks (hard to see); 2) hairline crack with efflorescence; 3) efflorescence; 4) defect-free concrete. Bottom row from left to right: 1) large spalled area with exposed bars and corrosion; 2) crack with graffiti; 3) corrosion stain, minor onset efflorescence; 4) defect-free concrete with dirt and markings.</span>

<img src="https://github.com/supervisely/supervisely/assets/78355358/beb55ba4-3d9f-4584-98ff-3ed3d58206f0" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">(b) From left to right: 1) spalled area with exposed bar, advanced corrosion and efflorescence; 2) exposed corroded bar; 3) larger crack; 4) partially exposed corroded bars, cracks; 5) hairline crack; 6) heavy spallation, exposed bars, corrosion; 7) wet/damp crack with efflorescence on the top; 8) efflorescence; 9) spalled area; 10) hairline crack with efflorescence.</span>

The acquisition of the CODEBRIM dataset stemmed from the necessity for a more comprehensive representation of overlapping defect classes, extending beyond previous research primarily focused on cracks. The authors meticulously curated and annotated the dataset, resulting in a rich resource for training and evaluating computer vision models.

The dataset encompasses:

* 1590 high-resolution images depicting defects within the context of 30 distinct bridges,
* 5354 annotated defect bounding boxes, often exhibiting overlapping defects, alongside 2506 generated non-overlapping background bounding boxes,
* Varied defect counts for distinct classes: crack (2507), spallation (1898), efflorescence (833), exposed bars (1507), and corrosion stain (1559).

<i>Note, that the number of objects in DatasetNinja may differ in comparison with the original dataset due to the conversion effects.</i>

The multi-target nature of the dataset adds complexity compared to single-class recognition benchmarks, as many instances exhibit more than one class simultaneously. Moreover, the task presents challenges related to variations in aspect ratio, scale, and resolution across different defects and their bounding boxes. These intricacies are crucial for developing effective defect recognition algorithms, as they mirror real-world scenarios in concrete infrastructure assessment. Further details and comprehensive distributions are available in the supplementary material in the Research Paper.
