from ultralytics import YOLO
import os

model = YOLO("./runs/detect/train5/weights/best.pt")

results = model.train(epochs=18, imgsz=640, batch=1, val=True) 
