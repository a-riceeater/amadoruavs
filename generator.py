import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage():
    shape = random.choice(shapes)
    letter = random.choice(letters)
    print(shape + " " + letter)

    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(40, 40), (220 - 10, 190 - 10)], fill="blue")

    image.save("vision.png")

    # TODO: Center image + colors + shape + potentially add noise?


generateImage()