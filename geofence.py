import numpy as np
import matplotlib.pyplot as plt

n = 0 # geofence coordinates (amt)
m = 0 # waypoint coordinates (amt)

fence = [] # fence coordinates
waypoints = [] # waypoint coordinates

with open("navigate.txt", "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            n, m = map(int, line.split(" "))
        elif i <= n:
            lat, lon = map(float, line.strip().split())
            fence.append((lat, lon))
        else:
            lat, lon = map(float, line.strip().split())
            waypoints.append((lat, lon))
        
x, y = zip(*fence)        
x2, y2 = zip(*waypoints)
plt.plot(y, x, linestyle='-', marker='o') 
plt.plot(y2, x2, color='green', linestyle='-', marker='o')
plt.show() 