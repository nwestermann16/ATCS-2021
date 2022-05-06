
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

#Load Data

dataGenre = pd.read_csv("data/SongData.csv")


#Turn non-numerical values into numbers and load data
#feature_genres = dataGenre["genres"].values
#genre_transformer = LabelEncoder().fit(feature_genres)
#feature_genres = genre_transformer.transform(feature_genres)

feature_danceability = dataGenre["danceability"].values
feature_instrumentalness = dataGenre["instrumentalness"].values
feature_speechiness = dataGenre["speechiness"].values
feature_popularity = dataGenre["popularity"].values

x = np.array([feature_danceability, feature_instrumentalness, feature_speechiness, feature_popularity]
             ).transpose()

#Standardize Data
scaler = StandardScaler().fit(x)
features = scaler.transform(x)


#inertias = []
#for k in range(1, 100):
      ## build model
      #kmeanModel = KMeans(n_clusters=k).fit(x)
#     ##store inertia
      #inertias.append(kmeanModel.inertia_)
# #Plot inertias to find the Elbow
#plt.plot(range(1, 100), inertias, "bx-")
#plt.xlabel("Values of K")
#plt.ylabel("Inertia")
#plt.title("The Elbow Method using Inertia")
#plt.show()

#Create Model
k = 5
km = KMeans(n_clusters=k).fit(x)

# Get the centroid and label values

centroids = km.cluster_centers_
labels = km.labels_

# Get user input


userSong = input("What is your favorite song?\n")

#finds song in data and gets index
song = dataGenre.loc[dataGenre['name'] == userSong]
index = song.index.values
print(index)

if len(index) > 1:
    index = index[0]
    # uses labels to find cluster
clusterNumber = labels[index]
print(clusterNumber)

# Print 10 songs from cluster that includes user input
print("Here is a playlist based on your favorite song:")
for i in range(1, 100):
    if labels[i] == clusterNumber:
        print(dataGenre.iloc[i]["name"])

# Get user input
userArtist = input("Who is your favorite artist\n")

#finds artist in data and gets index
artist = dataGenre.loc[dataGenre['artists'] == userArtist]
indexArtist = artist.index.values

if len(indexArtist) > 1:
    indexArtist = indexArtist[0]
# uses labels to find cluster
clusterNumberArtist = labels[indexArtist]

print("Here are some similar artists based on your favorite artist:")
for i in range(1, 100):
    if labels[i] == clusterNumberArtist:
        print(dataGenre.iloc[i]["artists"])


