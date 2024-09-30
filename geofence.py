import numpy as np

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
        
