import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(size, shape, character, color):
    print(shape + " " + character)

    x, y = random.randint(0, size[0]), random.randint(0, size[1])
    width, height = random.randint(50, 100), random.randint(50, 100)

    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x, y), (width, height)], fill="blue")
    

    image.save("vision.png")

    # TODO: Randomize location (and scale?) + colors + shape + rotate + position + potentially add noise?


generateImage((random.randint(500, 1000), random.randint(500, 1000)), "rectangle", random.choice(letters), "blue")