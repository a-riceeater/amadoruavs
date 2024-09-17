import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (100, 100)

    width, height = 100, 100
    x, y = random.randint(0, size[0]), random.randint(0, size[1])

    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    if shape == "rectangle":
        x, y = random.randint(0, size[0] - width), random.randint(0, size[1] - height)
        draw.rectangle([(0, 0), (100, 100)], fill=color)
    
        font = ImageFont.truetype("arial.ttf", 50)

        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((100-w)/2, (100-h)/2), character, font=font, fill="white")

    image.save("vision.png")


generateImage("rectangle", random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))