import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")
x = data[["Annual Income", "Spending Score"]]

#standardize the data
scaler = StandardScaler().fit_transform(x)

#the value of k has been defined for you
k = 5

#apply the kmeans algorithm
km = KMeans(n_clusters=k).fit(scaler)

#get the centroid and label values
centroids = km.cluster_centers_
labels = km.labels_

#sets the size of the graph
plt.figure(figsize=(5,4))

#use a for loop to plot the data points in each cluster
for i in range(k):
    cluster = scaler[labels == i]
    plt.scatter(cluster[:,0], cluster[:,1], label=f"Cluster {i+1}")

#plot the centroids
plt.scatter(centroids[:,0], centroids[:,1], color="black", marker="x", s=100, label="Centroids")
            
#shows the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()