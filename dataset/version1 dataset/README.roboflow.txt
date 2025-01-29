
Gap Detection - v1 2025-01-07 11:03am
==============================

This dataset was exported via roboflow.com on January 7, 2025 at 5:35 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 110 images.
Gap-up-or-gap-down are annotated in YOLOv11 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Randomly crop between 5 and 30 percent of the image
* Random brigthness adjustment of between -15 and +15 percent
* Random exposure adjustment of between -5 and +5 percent
* Random Gaussian blur of between 0 and 1 pixels
* Salt and pepper noise was applied to 0.53 percent of pixels


