from ultralytics import YOLO
import matplotlib.pyplot as plt
import bbox_visualizer as bbv
import cv2
from PIL import Image 
import numpy as np

model = YOLO("./runs/detect/train2/weights/best.pt")

results = model(["input.png"])
a = Image.open("input.png").convert("L")
a.save("input.png")

for result in results:
    bimg = bbv.draw_rectangle(a, results[0].boxes.data)
    plt.imshow(bimg)
    plt.show()