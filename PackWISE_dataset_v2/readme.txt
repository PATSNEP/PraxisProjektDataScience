PackWISE: Packaging Waste Instance Segmentation Dataset for Model Training and Evaluation

This dataset comprises 586 RGB images of post-consumer lightweight packaging waste captured on a conveyor belt. Annotations follow the COCO format. The samples were kindly provided by a recycling plant of Lobbe RSW GmbH in Iserlohn, Germany. Samples were recorded as received, with adherent contaminants and without pretreatment. This dataset is part of the multi-sensor-dataset of the project K3I-Cycling and funded by the Federal Ministry of Research, Technology and Space (BMFTR), Germany under the funding reference 033KI201.

Dataset details

    Images are provided as JPEG files of size 4096x4096 pixel.
    Annotations follow the COCO format: each instance is delineated by a pixel-level mask, a bounding-box, and assigned to one of 23 categories.
    Bounding box coordinates are given as Integers.
    Pixel masks are binary run-length encoded (RLE) and can be decoded using pycocotools.
    Annotations can be converted to YOLO format using the python script convert_dataset_to_yolo_format.py in the root folder of the dataset.
    This script generates text files (with categories and bounding boxes) for each image file and one yolo.yaml file in the folder named data.

Splits

    Training: 70%
    Validation: 15%
    Test: 15%

Image acquisition

    A prism-based RGB line-scan camera (SW-4000T-10GE) with a resolution of 4096 pixels was used.
    The line rate was set to 1278 lines per second.
    Two-dimensional images were reconstructed by scanning the samples as they moved along a conveyor belt at 0.2 m/s.
    Illumination was provided by 12 halogen lamps.

Access and metadata

    URL: https://fordatis.fraunhofer.de/handle/fordatis/463.2
    License: Creative Commons Attribution 4.0 (CC BY)
    Year: 2025
    Contributor: L. Roming, S. Rueger, M. Kalb, F. Beutler
