import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross", "semicircle"]

# star, and variating semicircle and quarter circle remaining
# also TODO: isolate ODLC from background to crop regardless of size or position for training data, then turn B&W? - thanks pratham btw
# nvm, either turn to greyscale (inefficent) or just remove color entirely and just set basic color

#   TODO: Optimize code / remove redundancy

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (200, 200)

    image = Image.new("RGBA", size, (255, 0, 0, 0))
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
        rand = random.randint(0, 3)
        if rand == 0:
            draw.pieslice((0, 0, 200, 200), start=270, end=360, fill=color)
            width, height = 270, 100
        elif rand == 1:
            draw.pieslice((0, 0, 200, 200), start=180, end=270, fill=color)
            width, height = 120, 100
        elif rand == 2:
            draw.pieslice((0, 0, 200, 200), start=0, end=90, fill=color)
            width, height = 270, 270
        else:
            draw.pieslice((0, 0, 200, 200), start=90, end=180, fill=color)
            width, height = 120, 270

    elif shape == "pentagon":
        draw.regular_polygon((100, 100, 100), 5, fill=color)
        width, height = 200, 200

    elif shape == "cross":
        draw.rectangle([(0, 75), (200, 125)], fill=color)
        draw.rectangle([(75, 0), (125, 200)], fill=color)
        width, height = 200, 200

    elif shape == "semicircle":
        if random.randint(0, 1) == 1:
            draw.pieslice((0, 0, 200, 200), start=180, end=360, fill=color)
            width, height = 200, 100
        else:
            draw.pieslice((0, 0, 200, 200), start=0, end=180, fill=color)
            width, height = 200, 300

    _, _, w, h = draw.textbbox((0, 0), character, font=font)
    draw.text(((width-w)/2, (height-h)/2), character, font=font, fill="white")

    rotation = random.randint(0, 360)
    image.save(f"vision.png", "PNG")
    i = Image.open("vision.png").rotate(rotation)
    i.save("vision.png", "PNG")
    img_colored = Image.open("vision.png")
    img_colored.load()
    alpha = img_colored.split()[-1]
    img_grey = img_colored.convert("L").convert("RGB")
    img_grey.putalpha(alpha)
    img_grey.save("vision.png")



imageAmount = 1

for i in range(imageAmount):
    generateImage("quarter circle", random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))