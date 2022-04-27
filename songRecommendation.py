
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

#Load Data
dataStats = pd.read_csv("data/SongData.csv")
dataGenre = pd.read_csv("data/data_w_genres.csv")


#Turn non-numerical values into numbers and load data
feature_genres = dataGenre["genres"].values
genre_transformer = LabelEncoder().fit(feature_genres)
feature_genres = genre_transformer.transform(feature_genres)

feature_danceability = dataGenre["danceability"].values
feature_instrumentalness = dataGenre["instrumentalness"].values
feature_speechiness = dataGenre["speechiness"].values
feature_popularity = dataGenre["popularity"].values

x = np.array([feature_genres, feature_danceability, feature_instrumentalness, feature_speechiness, feature_popularity]
             ).transpose()

#Standardize Data
scaler = StandardScaler().fit(x)
features = scaler.transform(x)

#Create Model
k = 5
km = KMeans(n_clusters=k).fit(x)

# Get the centroid and label values

centroids = km.cluster_centers_
labels = km.labels_

cluster = []
for i in range(k):
    cluster.append(x[labels == i])

userSong = input("What is your favorite song?\n")

print(cluster)

for i in range(k):
    for t in range(len(cluster[i])):
        clusterSearch = cluster[i][t]
        if clusterSearch == userSong:
            print(cluster[i])

