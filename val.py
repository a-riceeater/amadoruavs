from ultralytics import YOLO
import matplotlib.pyplot as plt
import bbox_visualizer as bbv
import cv2
from PIL import Image 
import numpy as np

model = YOLO("./runs/detect/train/weights/best.pt")
model.val()