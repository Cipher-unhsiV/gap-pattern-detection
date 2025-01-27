# CURRENT REQUIREMENT - P0
## PROGRESS
- Roboflow dataset (Original) - [link](https://universe.roboflow.com/workathon/gap-pattern)
- Dataset (Custom Augmented) - [link](https://universe.roboflow.com/starter-3re5h/gap-pattern-kjvnx)
- Model training version 1 - [link](https://colab.research.google.com/drive/1nn6zvGBYK-_tbNUUqQ0FxiaD2hGBKfU2?authuser=2#scrollTo=pGhEtUwTf67h)
- Version 1 with totally 110 data samples in yolo11s.
- Version 1 inference
  - Annotate Manually
  - Populate the dataset to 1000+
  - Accuracy low (suspect: low data samples)
- Version 2 trial with 900 training samples (Manual Annotation with Augmentation [300x3] via roboflow) in yolo11m
- Version 2 inference
  - Tested with 900 training samples (300 annotated x 3 r-augments) with much better decent results but yet to achieve the saturation!
  - Shifting from (96,9,5) split to (900,43,5) split has shown improved results. (train, valid, test)
  - 'mAP50' has increased by around 82 times and 'mAP50-95' has increased by around 148 times.
- Version 3 trial with more data samples, yolo11l and 25e:100e
