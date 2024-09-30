import pandas
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import geopandas

path = 'with outliers.txt'

coordinates = []

with open(path, 'r') as file:
    number_of_coordinates = int(file.readline().strip())
    
    for line in file:
        lat, lon = map(float, line.strip().split())
        coordinates.append((lat, lon))

longi, lat = zip(*coordinates)
plt.scatter(longi, lat)
plt.show()

X = np.asarray(coordinates)
dbscan = DBSCAN(eps=0.0002, min_samples=2)
dbscan.fit(X)

labels = dbscan.labels_

X_filtered = X[labels != -1]
filtered_labels = labels[labels != -1]

plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=filtered_labels, cmap='viridis', marker='o')
plt.title('dbscan clustering w/o outliers')
plt.xlabel('long')
plt.ylabel('lat')

unique_labels = set(filtered_labels)
for label in unique_labels:
    plt.scatter([], [], c=scatter.cmap(scatter.norm(label)), label=f'Cluster {label}')

plt.legend(title='Clusters')
plt.show()