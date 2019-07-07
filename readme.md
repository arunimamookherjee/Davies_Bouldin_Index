# Davies_Bouldin_Index
This partiular module has 3 main function:
    calculate_S:
        s is a measure of scatter within the cluster
        it makes this a Euclidean distance function between the centroid of the cluster, and the individual feature vectors.
        Si=Eucledian distance beteen centroid[i] which is the centroid of i and any point x in Xi

    calculate_Rij:
        Rij=Si+Sj/d
        d is the Euclidean distance between Cluster i and j

    calculate_R :
        we have 3 clusters right now:
        this function returns max[R01,R12, R20]


Libraries required:
sklearn
math
scipy
pandas
numpy


## Reference
http://www.turingfinance.com/clustering-countries-real-gdp-growth-part2/
