from ultralytics import YOLO
import cv2

model = YOLO("/content/best.pt")
input_image_path = "/content/Screenshot (135).png" 
results = model(input_image_path)
gap_up_count = 0
gap_down_count = 0
for result in results:
    boxes = result.boxes.xyxy 
    classes = result.boxes.cls  
    confidences = result.boxes.conf  
    for cls in classes:
        if cls == 0: 
            gap_down_count += 1
        elif cls == 1: 
            gap_up_count += 1
    annotated_image = result.plot() 
output_image_path = "output_image.jpg"
cv2.imwrite(output_image_path, annotated_image)
print(f"GAP UPs: {gap_up_count}")
print(f"GAP DOWNs: {gap_down_count}")
