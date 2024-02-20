<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>Box Detection in Warehouse Conveyor Belts</h1>
<p>This Repo contains a Box Detection Application capable of identifying box containers in conveyor belt pictures.</p>
<img src="https://github.com/abhijeetgupta23/Box-Detection-in-Warehouse-using-Vision-Based-ML-Engineering/assets/16919762/41706bd0-428b-4199-9917-7aea3bc9fb1c">

<h2>End User Instructions to run the Object Detection Model</h2>
In order to use this object detection web application, please follow below instructions

<ol>
  <li><strong>Install Docker</strong>
    <ul>
      <li>Make sure Docker is installed on your system. You can download and install Docker Desktop from the official Docker website.</li>
    </ul>
  </li>

  <li><strong>Pull the Docker Image</strong>
    <ul>
      <li>Open docker desktop, followed by a terminal or command prompt in your system and run:
        <pre><code>docker pull agpsuai23/box_detection_image</code></pre>
      </li>
      <li>This command will download the Docker image named <code>agpsuai23/box_detection_image</code> to your local machine.</li>
    </ul>
  </li>

  <li><strong>Run the Docker Container</strong>
    <ul>
      <li>Once the image is pulled, execute the following command:
        <pre><code>docker run -p 8000:8000 agpsuai23/box_detection_image</code></pre>
      </li>
      <li>This command starts the container and maps port 8000 of the host to port 8000 of the container, allowing access to the application.</li>
    </ul>
  </li>

  <li><strong>Access the Application</strong>
    <ul>
      <li>Open a web browser and go to: <a href="http://localhost:8000/" target="_blank">http://localhost:8000/</a></li>
      <li>You can now interact with the Box Detection Application through the browser interface.</li>
    </ul>
  </li>
</ol>
  
<h2>Project Details</h2>
<img src="https://github.com/abhijeetgupta23/Box-Detection-in-Warehouse-using-Vision-Based-ML-Engineering/assets/16919762/85cfbe9b-cab4-428b-9fca-5e699ea5d8b8">
<ol>
  <li><strong>Computer Vision based Data Science & ML</strong>
    <ul>
      <li><b>Yolo8_Model_Creation.ipynb</b> downloads the dataset from Roboflow, followed by training Yolov8 on train set using transfer learning, validation and test result display. We end up with a <b>mean Average Precision (mAP) of 0.913 (90%+)</b>. Finally, the model is saved as <b>best.pt</b></li>
    </ul>
  </li>

  <li><strong>Software Engineering using FAST API</strong>
    <ul>
      <li>I created a FastAPI web application <b>(main.py)</b> to serve the saved model to customers.</li> 
      <li>Home page <b>(Upload_for_Detection.html)</b> is a basic I/O based UI that lets a user upload a conveyor belt image, and when a button is clicked, the application uses the previously saved Yolo8 model to detect box containers and return the image with labels in a new page. Code can be found in main.py - @app.post("/YOLO_Box_Prediction_Website/") </li>
      <li>Alternatively, I also created an API functionality that can programmatically accept a conveyor belt image as input to return as output the image with labels saved in local system. Working can be found at  main.py - @app.post("/YOLO_Box_Prediction_Service/"). An example of API call can be found in <b>CUSTOM_YOLO_API_call.ipynb</b> </li>
      </ul>
  </li>
  <li><strong>Deployment using Docker Containerization</strong>
    <ul>
      <li>Finally, I deployed this FastAPI based Yolov8 application as a Docker Image (based on <b>Dockerfile</b>) and uploaded it to Docker Hub. 
      <li>All they need to do is to simply install Docker Desktop, pull the image from the hub, run it as a Docker container and finally access the webpage on a browser as localhost:8000</li>
      <li>Advantage of containerization is that all end users can avoid the hassle of installing packages mentioned in <b>requirements.txt</b>, which are necessary to run the application on their system.</li> 
    </ul>
  </li>
</ol>


</body>
</html>
