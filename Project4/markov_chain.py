###########################################
#             markov_chain.py             #
###########################################

import numpy as np
from numpy import random

N_ITER = 50

# Generate non-normalized Markov P matrix and normalize every row
P = random.rand(5, 5)

for row in range(P.shape[0]):
    P[row] /= sum(P[row])

# Generate transpose of normalized matrix
Pt = np.transpose(P)

# Generate initial p-vector and normalize
p50 = random.rand(5)
p50 /= sum(p50)

# Iteratively apply transition rule 
for i in range(N_ITER):
    p50 = np.matmul(Pt, p50)
    p50 /= sum(p50)
    
# print(p50)

# Generate eigenvalues and eigenvectors of transpose of P matrix
evals, evecs = np.linalg.eig(Pt)

# print(f"evals: {evals}")

# Extract eigenvector corresponding to eigenvalue of 1
evec = evecs[:,0]
evec /= sum(evec)

diff_vec = evec - p50
print(f"Stationary distribution according to iterative refinement: {p50}")
print(f"Stationary distribution according to matrix transpose: {evec}")
print(f"Difference between vectors: {sum(diff_vec)}")