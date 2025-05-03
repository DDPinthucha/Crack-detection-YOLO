import subprocess
import sys
import os

# Install pip
def install_libraries():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ultralytics"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "roboflow"])

# Install libraries
install_libraries()

# import libraries
from ultralytics import YOLO
import ultralytics
from roboflow import Roboflow

# check is ultralytics is installed
ultralytics.checks()

# Connect to your Roboflow API
rf = Roboflow(api_key="*******************")
project = rf.workspace("*******************").project("*******************")
version = project.version("*")

# Download dataset by YOLOv11 format
dataset = version.download("yolov11")

# Calling Model from terminal
data_yaml_path = os.path.join(dataset.location, "data.yaml")
subprocess.run([
    "yolo", 
    "task=detect",
    "mode=train",
    "model=yolo11n.pt",
    f"data={data_yaml_path}",
    "epochs=40",
    "imgsz=640",
    "batch=16",
    "lr0=0.005",
    "rect",
    "cache"
])
