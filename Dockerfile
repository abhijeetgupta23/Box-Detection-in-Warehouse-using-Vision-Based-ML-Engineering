# Dockerfile

# Use the official Python image as a base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

RUN apt-get update && apt-get install -y mesa-utils

RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Box_Detection_Yolo8_FastAPI

# Run main.py when the container launches
CMD ["python","-m", "uvicorn", "main:app","--host", "0.0.0.0", "--port","8000"]