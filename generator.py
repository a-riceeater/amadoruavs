import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (800, 800)

    width, height = 200, 150
    x, y = random.randint(0, size[0]), random.randint(0, size[1])

    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    if shape == "rectangle":
        x, y = random.randint(0, size[0] - width), random.randint(0, size[1] - height)
        draw.rectangle([x, y, x + width, y + height], fill=color)
    
        font = ImageFont.truetype("arial.ttf", 50)

        text_bbox = draw.textbbox((0, 0), character, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        text_x = x + (width - text_width) // 2
        text_y = y + (height - text_height) // 2

        draw.text((text_x, text_y), character, fill="white", font=font)



    image.save("vision.png")


generateImage("rectangle", random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))