from ultralytics import YOLO
import cv2
import gradio as gr

def gap_det(img):
    model = YOLO("best.pt")
    input_image_path = img
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
    annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    return annotated_image_rgb, gap_up_count, gap_down_count

with gr.Blocks() as demo:
    gr.Markdown("# GAP UP and GAP DOWN Detection")
    gr.Markdown("Upload an image to detect GAP UP and GAP DOWN patterns in stock market candlestick charts.")

    with gr.Row():
        input_image = gr.Image(label="Upload Image", type="filepath")
        output_image = gr.Image(label="Detected Image")
    
    with gr.Row():
        gap_up_output = gr.Textbox(label="GAP UP Count")
        gap_down_output = gr.Textbox(label="GAP DOWN Count")

    submit_button = gr.Button("Detect")
    submit_button.click(
        fn=gap_det,
        inputs=input_image,
        outputs=[output_image, gap_up_output, gap_down_output]
    )

demo.launch()