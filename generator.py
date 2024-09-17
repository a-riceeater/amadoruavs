import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross"]
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
        draw.text((200 // 2, 200 // 2), character, font=font, fill="white")

        #fix centering later

    image.save("vision.png")
    #image.save(f"vision-{shape}.png")


generateImage("triangle", random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))