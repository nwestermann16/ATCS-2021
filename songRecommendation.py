
import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#Load Data

dataGenre = pd.read_csv("data/SongData.csv")


feature_danceability = dataGenre["danceability"].values
feature_instrumentalness = dataGenre["instrumentalness"].values
feature_speechiness = dataGenre["speechiness"].values
feature_popularity = dataGenre["popularity"].values
feature_year = dataGenre["year"].values

x = np.array([feature_danceability, feature_instrumentalness, feature_speechiness, feature_popularity, feature_year]
             ).transpose()

scaler = StandardScaler().fit(x)
features = scaler.transform(x)

#Elbow method to get k
#inertias = []
#for k in range(1, 50):
      # build model
      #kmeanModel = KMeans(n_clusters=k).fit(x)
#     ##store inertia
      #inertias.append(kmeanModel.inertia_)
 #Plot inertias to find the Elbow
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

#Finds song in data and get index
song = dataGenre.loc[dataGenre['name'] == userSong]
index = song.index.values

#makes sure there is only one index value
if len(index) > 1:
    index = index[0]

# uses labels to find cluster
clusterNumber = labels[index]


# Print 10 songs from cluster that includes user input
print("Here is a playlist based on your favorite song:")
for i in range(1, 100):
    if labels[i] == clusterNumber:
        print(dataGenre.iloc[i]["name"])

#############

#Creates new model
feature_year2 = dataGenre["year"]
x2 = np.array([feature_popularity, feature_year]).transpose()

#Elbow method to get k


#Create Model
k_years = 5
km_years = KMeans(n_clusters=k).fit(x)

# Get the centroid and label values

centroids_years = km_years.cluster_centers_
labels_years = km.labels_

#Get user input
userYear = int(input("What is your favorite year of music? \n"))
#finds year in data and gets index
year = dataGenre.loc[dataGenre['year'] == userYear]
indexYear = year.index.values

#print(indexYear)

if len(indexYear) > 1:
    indexYear = indexYear[0]

# uses labels to find cluster
clusterNumberYear = labels_years[indexYear]

print("Here are some songs produced in " + str(userYear) + ":")
for i in range(1, 100):
    if labels_years[i] == clusterNumberYear:
        print(dataGenre.iloc[i]["name"])


