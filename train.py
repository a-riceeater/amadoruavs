from ultralytics import YOLO
import os

model = YOLO("./model/yolov8m.yaml")
results = model.train(data=os.path.join(os.getcwd(), "model", "model.yml"), epochs=2, imgsz=640, batch=1, val=True, pretrained=True) 
