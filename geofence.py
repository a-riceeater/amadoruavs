import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString

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
        
fence_polygon = Polygon(fence)

for i in range(len(waypoints) - 1):
    start = waypoints[i]
    end = waypoints[i + 1]
    path = LineString([start, end])

    if fence_polygon.contains(path):
        print(f"{start}, {end} segment intersects with path {waypoints[i]}")
        
        # shrink path somehow

x, y = zip(*fence)        
x2, y2 = zip(*waypoints)
plt.plot(y, x, linestyle='-', marker='o') 
plt.plot(y2, x2, color='green', linestyle='-', marker='o')
plt.show()
