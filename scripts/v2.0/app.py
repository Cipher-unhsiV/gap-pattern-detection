import requests
import pandas as pd
import plotly.graph_objects as go
from ultralytics import YOLO
import cv2
import os
import gradio as gr

API_KEY = "ITWJ6NDTF45CBTDO"  # Consider using environment variables for API keys

def get_stock_candlestick_data(symbol, interval="1min", output_size="compact"):
    """Fetch stock candlestick data from Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}&outputsize={output_size}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if f"Time Series ({interval})" in data:
            return data[f"Time Series ({interval})"]
        else:
            return None
    else:
        return None

def process_stock_candlestick_data(data):
    """Process Alpha Vantage stock candlestick data into a DataFrame."""
    if not data:
        return None
        
    rows = []
    for timestamp, values in data.items():
        rows.append({
            "timestamp": timestamp,
            "open": float(values["1. open"]),
            "high": float(values["2. high"]),
            "low": float(values["3. low"]),
            "close": float(values["4. close"]),
            "volume": float(values["5. volume"])
        })
    df = pd.DataFrame(rows)
    df = df.sort_values("timestamp")  # Ensure chronological order
    return df

def generate_candlestick_chart(df, n=50, output_path="candlestick.png"):
    """Generate a candlestick chart using Plotly with the last n data points."""
    if df is None or len(df) == 0:
        return None
        
    df = df.tail(n)  # Use only the last n rows
    fig = go.Figure(data=[go.Candlestick(
        x=df["timestamp"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"]
    )])
    fig.update_layout(
        title="Candlestick Chart",
        xaxis_title="Time",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False
    )
    fig.write_image(output_path)
    return output_path

def yolo_model(img_path, model_path):
    """Run YOLO model on the image and count GAP UP and GAP DOWN patterns."""
    if not os.path.exists(img_path):
        return None, 0, 0
        
    # Load model each time to avoid persistence issues in Spaces
    try:
        model = YOLO(model_path)
        results = model(img_path)
        gap_up_count = 0
        gap_down_count = 0
        
        for result in results:
            boxes = result.boxes
            if hasattr(boxes, 'cls') and len(boxes.cls) > 0:
                classes = boxes.cls.cpu().numpy() if hasattr(boxes.cls, 'cpu') else boxes.cls
                for cls in classes:
                    if int(cls) == 0:
                        gap_down_count += 1
                    elif int(cls) == 1:
                        gap_up_count += 1
                        
        annotated_image = results[0].plot()
        output_path = "annotated_output.png"
        cv2.imwrite(output_path, annotated_image)
        return output_path, gap_up_count, gap_down_count
    except Exception as e:
        print(f"Error running YOLO model: {e}")
        return None, 0, 0

def detect_gap_patterns(symbol, model_path="best.pt"):
    """Non-streaming function to fetch data, generate charts, and detect GAP patterns."""
    # Check if the model file exists
    if not os.path.exists(model_path):
        return None, f"Model not found at {model_path}", f"Model not found at {model_path}"
    
    # Get stock data
    data = get_stock_candlestick_data(symbol)
    if not data:
        return None, "Failed to fetch stock data", "Failed to fetch stock data"
    
    # Process data and generate chart
    df = process_stock_candlestick_data(data)
    if df is None or len(df) == 0:
        return None, "No valid stock data available", "No valid stock data available"
    
    chart_path = generate_candlestick_chart(df, n=50)
    if not chart_path or not os.path.exists(chart_path):
        return None, "Failed to generate chart", "Failed to generate chart"
    
    # Run YOLO detection
    annotated_path, gap_up_count, gap_down_count = yolo_model(chart_path, model_path)
    if not annotated_path:
        return None, "Failed to run detection model", "Failed to run detection model"
    
    return annotated_path, f"GAP UP Count: {gap_up_count}", f"GAP DOWN Count: {gap_down_count}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# GAP Pattern Detection in Stock Charts")
    gr.Markdown("Enter a stock symbol (e.g., AAPL) to detect GAP UP and GAP DOWN patterns in candlestick charts.")

    with gr.Row():
        symbol_input = gr.Textbox(label="Stock Symbol", placeholder="Enter a stock symbol (e.g., AAPL)")
        submit_button = gr.Button("Detect Patterns")

    with gr.Row():
        output_image = gr.Image(label="Annotated Candlestick Chart")
        
    with gr.Row():
        gap_up_output = gr.Textbox(label="GAP UP Results")
        gap_down_output = gr.Textbox(label="GAP DOWN Results")

    # Run detection when the button is clicked
    submit_button.click(
        fn=detect_gap_patterns,
        inputs=symbol_input,
        outputs=[output_image, gap_up_output, gap_down_output]
    )

# Launch the Gradio app
demo.launch()
