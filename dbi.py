from sklearn.cluster import k_means
from sklearn import datasets
import math
from scipy.spatial import distance
import pandas as pd
import numpy as np


def calculate_s(i, X, cluster_labels, centroids):
    '''
    :return: s is a measure of scatter within the cluster
    it makes this a Euclidean distance function between the centroid of the cluster, and the individual feature vectors.
    '''
    scatter = 0
    for X in cluster_labels:
        scatter +=distance.euclidean(centroids[i],X)
    return scatter


def calculate_Rij(i, j, X, cluster_labels, centroids):
    '''
    :return: A solution that satisfies these properties is: Rij= (Si+Sj)/Mij
    :mij= is a measure of separation between cluster Ci and Cj. It is euclidian distance
    '''


    # print("centroids" +str(centroids[i]), str(centroids[j]), " distance"+ str(distance.euclidean(centroids[i],centroids[j])))
    #print("calling Calculate s "+ str(calculate_s(i,X,cluster_labels,centroids)))

    mij= distance.euclidean(centroids[i],centroids[j])
    Rij = (calculate_s(i, X, cluster_labels, centroids) + calculate_s(j, X, cluster_labels, centroids)) / mij
    return Rij



def calculate_R( X, cluster_labels, centroids, no_of_clusters):
    '''
    :return:
    suppose we have 3 clusters right now:
    this function returns max[d(0)+(d1)/d(01)],[d(1)+d(2)/d(12)], [d(2)+d(0)/d(20)]

    '''
    values_of_r = []
    for i in range(no_of_clusters):
        for j in range(no_of_clusters):
            if(i!=j):
                temp = calculate_Rij(i, j, X, cluster_labels, centroids)
                values_of_r.append(temp)
    return max(values_of_r)

def calculate_dbi(X, cluster_labels, centroids, no_of_clusters):
    R = 0
    for i in range(no_of_clusters):
        R = R + calculate_R(X , cluster_labels, centroids, no_of_clusters)

    dbi= float(R) / float(no_of_clusters)
    return dbi

def main():

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    no_of_clusters = 3
    clf = k_means(X, n_clusters=no_of_clusters)
    centroids = clf[0]
    cluster_labels = clf[1]
    '''print("CENTROIDS...")
    print (centroids)
    print("CLUSTER LABELS...")
    print(cluster_labels)'''

    print("\n\n DBI:::    "+str(calculate_dbi(X, cluster_labels, centroids, no_of_clusters)))


if __name__ == "__main__":
    main()
