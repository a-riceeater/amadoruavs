import numpy as np
import random
# from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import time
import math
import matplotlib.pyplot as plt
import bbox_visualizer as bbv
import cv2
import os

shapes = ["circle", "quarter circle", "triangle", "rectangle", "pentagon", "star", "cross", "semicircle"]
shapeLetters = {}
# todo: optimize repeated code, fix bounding box for quarter circles

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateYAML():
    print("GENERATING YAML")
    outputPath = os.path.join(os.getcwd(), "model")
    trainPath = os.path.join(os.getcwd(), "model", "train")
    labelPath = os.path.join(os.getcwd(), "model", "labels")

    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    if not os.path.exists(trainPath):
        os.makedirs(trainPath)
        print("created directory")

    if not os.path.exists(labelPath):
        os.makedirs(labelPath)
        print("created directory")
    
    f = open(os.path.join(outputPath, "model.yml"), "w")
    print(outputPath)

    text = "path: ./\ntrain: ./images/train\nval: ./images/val\n\nnames:\n"

    num = 0
    for shape in shapes:
        for letter in letters:
            text += f"\n  {num}: {shape} {letter}"
            shapeLetters[f"{shape} {letter}"] = num
            num += 1
    
    f.write(text)
    f.close()

generateYAML()


def generateImage(shape, character, color, count, output):
    print(shape + " " + character)
    size = (200, 200)

    image = Image.new("RGBA", size, (0, 0, 0, 0))
    image = Image.new("RGBA", size, (0, 0, 0, 0))
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
    draw.text(((width - w) / 2, (height - h) / 2), character, font=font, fill="white")

    rotation = random.randint(0, 360)

    image.save(f"./model/images/{output}/vision-{count}.png", "PNG")

    img_straight = Image.open(f"./model/images/{output}/vision-{count}.png").rotate(rotation, expand=True)
    img_straight.save(f"./model/images/{output}/vision-{count}.png", "PNG")

    img_straight = img_straight.convert("LA")
    img_straight.save(f"./model/images/{output}/vision-{count}.png", "PNG")

    completed = Image.open(f"./model/images/{output}/vision-{count}.png")
    pix = completed.load()
    
    xmin = completed.width
    xmax = 0
    ymin = completed.height
    ymax = 0
    
    for x in range(completed.width):
        for y in range (completed.height):
            cp = pix[x, y]
            #print(cp)
            if cp[0] != 0 and cp[1] != 0: #and cp[2] != 0 and cp[3] != 0: # weird comparison bcus python tuples are weird
                if x < xmin:
                    xmin = x
                if x > xmax:
                    xmax = x
                if y < ymin:
                    ymin = y
                if y > ymax: 
                    ymax = y

    # debug bounding box checking, will remove later


    print((xmin, ymin, xmax, ymax))
    img = cv2.imread(f"./model/images/{output}/vision-{count}.png")
    bimg = bbv.draw_rectangle(img, (xmin, ymin, xmax, ymax))
    #plt.imshow(bimg)
    #plt.show()


    label = open(f"./model/labels/{output}/vision-{count}.txt", "w")
    sc = f"{shape} {character}"

    x_center = (xmin + xmax) / (2 * completed.width)
    y_center = (ymin + ymax) / (2 * completed.height)
    width = (xmax - xmin) / completed.width
    height = (ymax - ymin) / completed.height


    label.write(f"{shapeLetters[sc]} {x_center} {y_center} {width} {height}")
    label.close()

imageAmount = 100
start = time.time()
for i in range(imageAmount):
    generateImage(random.choice(shapes), random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), i, "train")


for i in range(20): # generate 20% of the images created for validation
    generateImage(random.choice(shapes), random.choice(letters), (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), i, "val")
