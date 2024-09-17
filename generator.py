import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross", "semicircle"]

# star, cross, semicircle, quarter circle remaining
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (200, 200)

    image = Image.new("RGB", size)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 50)

    if shape == "rectangle":
        width, height = 200, 100
        draw.rectangle([(0, 0), (200, 100)], fill=color)
        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((width-w)/2, (height-h)/2), character, font=font, fill="white")

    elif shape == "triangle":
        draw.polygon([(100,0), (0,200), (200, 200)], fill=color)
        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((200-w)/2, (250-h)/2), character, font=font, fill="white")   

    elif shape == "circle":
        draw.ellipse((0, 0, 200, 200), fill=color)
        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((200-w)/2, (200-h)/2), character, font=font, fill="white")

    elif shape == "quarter circle":
        draw.pieslice((-50, -50, 200, 200), start=0, end=90, fill=color)
        # figure out sizing and text placement later

    elif shape == "pentagon":
        draw.regular_polygon((100, 100, 100), 5, fill=color)
        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((200-w)/2, (200-h)/2), character, font=font, fill="white")

    elif shape == "cross":
        draw.rectangle([(0, 50), (200, 100)], fill=color)
        draw.rectangle([(100 / 2, 0), (150, 200)], fill=color)
        _, _, w, h = draw.textbbox((0, 0), character, font=font)
        draw.text(((200-w)/2, (200-h)/2), character, font=font, fill="white")

    image.save("vision.png")
    #image.save(f"vision-{shape}.png")


generateImage("cross", random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))