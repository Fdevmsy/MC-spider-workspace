from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from scipy.sparse import csr_matrix


X = [[0, 1], [7, 1], [5, 1], [1, 2], [0, 2]]


# x is the matrix which indicts all the points
def dist(x): 
    dist = euclidean_distances(x)
    return dist

# return the index of the nearest points for every given points 
def NNeighbor(mat):
    idx = list()
    distMatrix = dist(mat)
    distMatrix = csr_matrix(distMatrix)
#     print(distMatrix)
    for i in range(distMatrix.shape[0]):
        row = distMatrix.getrow(i).toarray()[0].ravel()
        top_indices = row.argsort()[1]
        # print(top_indices)
        top_values = row[row.argsort()[1]]
#         print top_indices
        # print(top_values)
        idx.append(top_indices)
    return idx


print(NNeighbor(X))


