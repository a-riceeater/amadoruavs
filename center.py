import pandas
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import geopandas


def getCenters(fp):
    """
    Args:
        fp (string): file path containing coordinates

    Returns:
        string: contains centeroids of clusters (rounded to 5 decimal places)
    """
    coordinates = []

    with open(fp, 'r') as file:
        file.readline().strip()

        for line in file:
            lat, lon = map(float, line.strip().split())
            coordinates.append((lat, lon))

    X = np.asarray(coordinates)
    db = DBSCAN(eps=0.00002, min_samples=5)
    db.fit(X)
    labels = db.labels_
    unique_labels = set(labels)

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    # print("Estimated number of clusters: %d" % n_clusters_)
    # print("Estimated number of noise points: %d" % n_noise_)

    centroids = []

    for k in unique_labels:
        if k == -1:
            continue
        class_member_mask = labels == k
        cluster_points = X[class_member_mask]
    
        centroid = np.mean(cluster_points, axis=0)
        centroids.append(centroid)

    return "\n".join(f"{round(centroid[0], 5)}, {round(centroid[1], 5)}" for centroid in centroids)


# optional visual display of plotting
def display(labels, db, centroids, n_clusters, X):
    unique_labels = set(labels)
    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True


    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]

        class_member_mask = labels == k

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor=(1, 1, 1, 0),
            markersize=6,
        )

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor=(1, 1, 1, 0),
            markersize=6,
        )


    for centroid in centroids:
        plt.plot(centroid[0], centroid[1], 'X', color='red', markersize=15, label=f'Centroid {k}')

    plt.title(f"Estimated number of clusters: {n_clusters}")
    plt.show()

centers = getCenters('with outliers.txt')
print(centers)