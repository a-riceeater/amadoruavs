import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import time
import math
import matplotlib.pyplot as plt
import bbox_visualizer as bbv
import cv2

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross", "semicircle"]

# todo: optimize repeated code, fix bounding box for quarter circles

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateImage(shape, character, color):
    print(shape + " " + character)
    size = (200, 200)

    image = Image.new("RGBA", size, (255, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 50)

    width, height = 200, 200
    bbox = None

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
    
    elif shape == "star":
        outer_radius = 80
        inner_radius = 35
        center = (100, 100)
        points = []

        def get_point(center, radius, angle):
            x = center[0] + radius * math.cos(math.radians(angle))
            y = center[1] - radius * math.sin(math.radians(angle))
            return (x, y)
        
        for i in range(10):
            radius = outer_radius if i % 2 == 0 else inner_radius
            angle = i * 36
            points.append(get_point(center, radius, angle))

        draw.polygon(points, fill=color)

    _, _, w, h = draw.textbbox((0, 0), character, font=font)
    draw.text(((width-w)/2, (height-h)/2), character, font=font, fill="white")

    rotation = random.randint(0, 360)

    image.save(f"vision.png", "PNG")

    img_straight = Image.open("vision.png").rotate(rotation, expand=True)
    img_straight.save("vision.png", "PNG")
    
    img_colored = Image.open("vision.png")
    img_colored.load()
    alpha = img_colored.split()[-1]
    img_grey = img_colored.convert("L").convert("RGB")
    img_grey.putalpha(alpha)
    img_grey.save("vision.png")

    completed = Image.open("vision.png")
    pix = completed.load()
    
    xmin = completed.width
    print(completed.width)
    xmax = 0
    ymin = completed.height
    ymax = 0
    
    for x in range(completed.width):
        for y in range (completed.height):
            cp = pix[x, y]
            if cp[0] != 0 and cp[1] != 0 and cp[2] != 0 and cp[3] != 0: # weird comparison bcus python tuples are weird
                if x < xmin:
                    xmin = x
                    print(f"XMIN FOUND FROM {xmin} to {x}, {y}, {pix[x,y]}, {pix[x, y] != (0, 0, 0, 0)}")
                if x > xmax:
                    xmax = x
                    print(f"XMAX FOUND FROM {xmax} to {x}, {y}, {pix[x,y]}, {pix[x, y] != (0, 0, 0, 0)}")
                if y < ymin:
                    ymin = y
                if y > ymax: 
                    ymax = y
    print(f"(xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax})")

    # debug bounding box checking, will remove later

    img = cv2.imread("vision.png")
    bimg = bbv.draw_rectangle(img, (xmin, ymin, xmax, ymax))
    plt.imshow(bimg)
    plt.show()

imageAmount = 1
start = time.time()
for i in range(imageAmount):
    generateImage(random.choice(shapes), random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))