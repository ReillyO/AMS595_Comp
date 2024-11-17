######################################
#             page rank              #
######################################

import numpy as np
import scipy as sp

# define probability matrix
M = np.array([[0.0, 0.0, 0.5, 0.0],
              [1/3, 0.0, 0.0, 0.5],
              [1/3, 0.5, 0.0, 0.5],
              [1/3, 0.5, 0.5, 0.0]])

# print(M[:,1]) # debug

# calculate eigenvectors of matrix and pick dominant to represent PageRank
evals, evecs = sp.linalg.eig(M)
dom_evec = evecs[0]
print(evecs)

# normalize PageRanks
dom_evec /= sum(dom_evec)

# initialize variables for convergence analysis
v = np.array([1,1,1,1])
v0 = np.zeros(4)
diff = sum(abs(v0-v))

# iteratively simulate convergence of probabilities to PageRanks
while diff > 0.00001:
    v0 = v
    v = np.matmul(M,v)
    v /= sum(v)
    #print(v)
    #print(v0)
    diff = abs(sum(v0-v))