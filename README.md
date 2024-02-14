<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>Object-Detection-for-ML-Engineering Image</h1>
<p>This Repo contains a Box Detection Application capable of identifying box containers in conveyor belt pictures.</p>

<h2>Usage Instructions</h2>

<ol>
  <li><strong>Install Docker</strong>
    <ul>
      <li>Make sure Docker is installed on your system. You can download and install Docker Desktop from the official Docker website.</li>
    </ul>
  </li>

  <li><strong>Pull the Docker Image</strong>
    <ul>
      <li>Open a terminal or command prompt in your system and run:
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

</body>
</html>
