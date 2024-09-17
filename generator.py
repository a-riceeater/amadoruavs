import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross", "semicircle"]

# star, and variating semicircle and quarter circle remaining
# also TODO: isolate ODLC from background to crop regardless of size or position for training data, then turn B&W? - thanks pratham btw
# nvm, either turn to greyscale (inefficent) or just remove color entirely and just set basic color

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (200, 200)

    image = Image.new("RGB", size)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 50)

    width, height = 200, 200

    if shape == "rectangle":
        width, height = 200, 100
        draw.rectangle([(0, 0), (200, 100)], fill=color)

    elif shape == "triangle":
        draw.polygon([(100,0), (0,200), (200, 200)], fill=color)
        width, height = 200, 250

    elif shape == "circle":
        draw.ellipse((0, 0, 200, 200), fill=color)
        width, height = 200, 200

    elif shape == "quarter circle":
        draw.pieslice((0, 0, 200, 200), start=270, end=360, fill=color)
        width, height = 270, 100

    elif shape == "pentagon":
        draw.regular_polygon((100, 100, 100), 5, fill=color)
        width, height = 200, 200

    elif shape == "cross":
        draw.rectangle([(0, 75), (200, 125)], fill=color)
        draw.rectangle([(75, 0), (125, 200)], fill=color)
        width, height = 200, 200

    elif shape == "semicircle":
        draw.pieslice((0, 0, 200, 200), start=180, end=360, fill=color)
        width, height = 200, 100

    _, _, w, h = draw.textbbox((0, 0), character, font=font)
    draw.text(((width-w)/2, (height-h)/2), character, font=font, fill="white")

    image.convert("L")
    image.save(f"vision.png")



imageAmount = 1

for i in range(imageAmount):
    generateImage(random.choice(shapes), random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))