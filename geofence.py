import numpy as np

n = 0 # geofence coordinates (amt)
m = 0 # waypoint coordinates (amt)

with open("navigate.txt", "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            n, m = map(int, line.split(" "))
