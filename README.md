# **GAP Pattern Detection in Candlestick Charts**

![Project Banner](https://github.com/user-attachments/assets/dc0e5bc8-dae4-4ec6-9721-929ddc2c0460)  
*Automating the detection of GAP UP and GAP DOWN patterns in candlestick charts using YOLO object detection.*

---
<p align="center">
<a href="https://universe.roboflow.com/cipherunhsiv/gap-pattern-detection">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>
<a href="https://universe.roboflow.com/cipherunhsiv/gap-pattern-detection/model/">
    <img src="https://app.roboflow.com/images/try-model-badge.svg"></img>
</a>
</p>

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Key Concepts](#key-concepts)
   - [Candlestick Charts](#candlestick-charts)
   - [GAP UP and GAP DOWN](#gap-up-and-gap-down)
3. [Project Details](#project-details)
   - [How It Works](#how-it-works)
   - [Class Types](#class-types)
   - [Model Training](#model-training)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running the Project](#running-the-project)
5. [Try It Online](#try-it-online)
6. [Dataset](#dataset)
7. [Technologies Involved](#technologies-involved)
8. [Successor Note](#successor-note)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)

---

## **Project Overview**

This project focuses on detecting **GAP UP** and **GAP DOWN** patterns in **candlestick charts**, which are widely used in technical analysis for stock market trading. Using a **YOLOv11l** (You Only Look Once) object detection model, the project identifies these patterns in candlestick chart images. The model is trained on a custom dataset and can be used to analyze charts for potential market movements.

It is designed to help traders and analysts quickly identify GAP patterns, saving time and improving accuracy in technical analysis. It includes a **Gradio-based web interface** for easy interaction and real-time detection.

---

## **Key Concepts**

### **Candlestick Charts**
Candlestick charts are a type of financial chart used to represent the price movement of an asset (e.g., stocks, cryptocurrencies) over time. Each "candlestick" consists of:
- **Body**: Represents the opening and closing prices.
- **Wicks (or Shadows)**: Represent the highest and lowest prices during the time period.

Candlestick charts are widely used in technical analysis to identify trends, reversals, and patterns.



### **GAP UP and GAP DOWN**
- **GAP UP**: Occurs when the **lowest price of the current candlestick is higher than the highest price of the previous candlestick**. This indicates a strong upward momentum and is often considered a bullish signal.
- **GAP DOWN**: Occurs when the **highest price of the current candlestick is lower than the lowest price of the previous candlestick**. This indicates a strong downward momentum and is often considered a bearish signal.

These patterns are significant because they can signal potential breakouts or reversals in the market.

---

## **Project Details**

### **How It Works**
1. **Input**: The user uploads an image of a candlestick chart or interacts with the Gradio interface.
2. **Detection**: The YOLOv11l model processes the image to detect GAP UP and GAP DOWN patterns.
3. **Output**: An annotated image with detected patterns highlighted, along with counts of GAP UP and GAP DOWN patterns.

### **Class Types**
The YOLO model is trained to detect two classes:
- **Class 0**: GAP DOWN
- **Class 1**: GAP UP

### **Model Training**
- The model is trained on a custom dataset of annotated candlestick charts.
- The dataset includes images with labeled GAP UP and GAP DOWN patterns.
- The model is saved as `best.pt` and loaded for inference.

---

## **Getting Started**

### **Prerequisites**
To run this project locally, you need:
- Python 3.8 or higher
- Pip (Python package manager)
- A GPU (recommended for faster inference)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gap-pattern-detection.git
   cd gap-pattern-detection
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Running the Project**
1. Download the trained model weights (```best.pt```) from the [Roboflow dataset page](https://universe.roboflow.com/cipherunhsiv/gap-pattern-detection) and place it in the ```models``` directory.
2. Run the Gradio interface:
   ```bash
   python app.py
   ```
3. The output will be saved as output_image.jpg in the results directory.

## Try It Online
You can try the project without installing anything locally by using the Hugging Face Spaces deployment:
👉 [GAP Pattern Detection on Hugging Face](https://huggingface.co/spaces/cipherunhsiv/gap-pattern-detection)

## Dataset
The dataset used for training the model is publicly available on Roboflow. You can access it here:
🔗 [Roboflow Dataset: GAP Pattern Detection](https://universe.roboflow.com/cipherunhsiv/gap-pattern-detection)

The dataset includes:
- Annotated images of candlestick charts.
- Labels for GAP UP and GAP DOWN patterns.

## Technologies Involved

- **YOLOv11l**: For object detection.
- **Gradio**: For creating a user-friendly web interface.
- **OpenCV (cv2)**: For image processing and annotation.
- **Roboflow**: For dataset management and annotation.

## Successor Note 
We’re excited to announce that **Version 2** of this project is currently in development! While we can’t reveal all the details just yet, here’s a sneak peek at what’s coming:
- **Real-Time Market Insights**: Version 2 will take GAP pattern detection to the next level by integrating live market data. Imagine detecting GAP patterns as they form, in real-time!
- **Enhanced User Experience**: A more dynamic and interactive interface that adapts to real-time changes in the market.
- **Advanced Analytics**: New features to help you gain deeper insights into market trends and patterns.

Stay tuned for updates as we work on bringing these exciting new features to life. _The future of GAP pattern detection is just around the corner!_

## Contributing
We welcome contributions to improve the model, dataset, or interface. Here’s how you can contribute:

1. Fork the repository and clone it:

   ```bash
   git clone https://github.com/your-username/gap-pattern-detection.git```

2. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your message here"```

4. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature-name```

5. Open a Pull Request on the main repository.

## Labeling Guidelines

If you’re labeling new data for the dataset, follow these guidelines:

- Use a labeling tool like LabelImg or CVAT.
- For each GAP UP or GAP DOWN pattern:
  - Draw a bounding box around the two candlesticks involved in the pattern.
  - Assign the correct class label (0 for GAP DOWN, 1 for GAP UP).
- Ensure the bounding boxes are tight and accurate.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Roboflow](https://roboflow.com/) for providing the dataset and annotation tools.
- [Ultralytics](https://www.ultralytics.com/) for the YOLO object detection framework.
- [Gradio](https://www.gradio.app/) for the web interface framework.
- [HF Spaces](https://huggingface.co/spaces) for the deployment platform.

## Connect

- GitHub: [Cipher-unhsiV](https://github.com/Cipher-unhsiV)
- Email: vishnuvasants@gmail.com
- LinkedIn: [Vishnuvasan T S](https://www.linkedin.com/in/cipher-unhsiv)


<strong><p align="center">Happy Trading and Coding! 🚀</p></strong>
   
