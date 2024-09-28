from ultralytics import YOLO
import matplotlib.pyplot as plt
import bbox_visualizer as bbv
import cv2
from PIL import Image 
import numpy as np

model = YOLO("./runs/detect/train/weights/best.pt")

results = model(["input.png"])
a = Image.open("input.png")
a = np.asarray(a)
for result in results:
    bimg = bbv.draw_rectangle(a, results[0].boxes.data)
    plt.imshow(bimg)
    plt.show()