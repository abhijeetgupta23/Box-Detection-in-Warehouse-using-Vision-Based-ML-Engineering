import matplotlib.pyplot as plt
from ultralytics import YOLO
from PIL import Image
from typing import List, Any
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import os
import requests

app = FastAPI()

# Define endpoint for home page that accepts images
@app.get("/")
async def read_index():
    return FileResponse('Upload_for_Detection.html')

# Define endpoint for making box predictions using Web UI
@app.post("/YOLO_Box_Prediction_Website/")
def predict_uploaded_image(file: UploadFile):

    try:

        # Upload and open the image transmitted via POST in a file based on its name
        file_name = file.filename
        with open(file_name, "wb") as f:
            f.write(file.file.read())

        # Obtain box detection result
        best_model_source = 'best.pt'
        yolov8_box_detection = YOLO(best_model_source)
        results = yolov8_box_detection(file_name)  

        # Plot the results on image and display it
        im_array = results[0].plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('example_output.jpg')  # save image
        output_path = Path("example_output.jpg")    
        return FileResponse(output_path)
        
    except Exception as e:
        return {"message": e.args}
    
# Define endpoint for making box predictions programatically
@app.post("/YOLO_Box_Prediction_Service/")
async def predict_uploaded_image(file: UploadFile):

    try:

        # Upload the image transmitted via POST in a file based on its name
        file_name = file.filename
        with open(file_name, "wb") as f:
            f.write(await file.read())

        # Obtain box detection result
        best_model_source = 'best.pt'
        yolov8_box_detection = YOLO(best_model_source)
        results = yolov8_box_detection(file_name)  

        # Plot the results on image and display it
        im_array = results[0].plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('example_output.jpg')  # save image
        output_path = Path("example_output.jpg")    
       
        # Get metadata about the file
        file_name = os.path.basename(output_path)
        file_size = os.path.getsize(output_path)
        
        # Create a dictionary containing file metadata
        file_metadata = {
            "file_name": file_name,
            "file_size": file_size
        }
        
        # Return JSON response containing file metadata along with the file data
        return {"file_metadata": file_metadata, "file_data": FileResponse(output_path)}
        
    except Exception as e:
        return {"message": e.args}