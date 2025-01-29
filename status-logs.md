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
  - Shifting from **(32,9,5)** split to **(96,9,5)** split to finally **(900,43,5)** split has shown improved results. (train, valid, test)
  - 'mAP50' has increased by around 82 times and 'mAP50-95' has increased by around 148 times.
- Version 3 trial with more data samples, yolo11l and 25e:100e
  - Tested with 1374 training samples and split being **(1374,50,0)**.
  - yolo11x seemed to be too complex for this task and was easily overfitting - so neglected!
  - yolo11l seemed comparatively better that yolo11x with decent results.
- **Version 3 is the best possible saturation with yolo via cli. Trying pythonic way may (or may not) give better control over arguments that could pave way to enhanced results.**

## SUMMARY
![Image](https://github.com/user-attachments/assets/8e593355-96e1-499a-99ee-d8ff2bb58c7f)

## RESULTS

### Test Image
![Image](https://github.com/user-attachments/assets/4455a8dc-6465-4f2f-9dd3-488061d85303)

## Corresponding Output
![Image](https://github.com/user-attachments/assets/54a11770-9bf7-410f-8371-224990d60d47)
