######################################
#               PCA                  #
######################################
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
data = np.transpose(data)
plt.plot(data[0,:], data[1,:], "bo", label="Original data")

covar = np.cov(data)

evals, evecs = sp.linalg.eigh(covar)
count=0

print(covar.shape)

for eval in evals:
    print(f"Principle Component {count}:\nEigenvalue: {eval}\nEigenvector: {evecs[count]}\n")
    count += 1
print(f"Largest Principle Component:\nEigenvalue: {evals[evals.argmax()]}\nEigenvector: {evecs[evals.argmax()]}")

# flattened_0 = [evecs[0][0]*data[0,:], evecs[0][1]*data[0,:]]
# hard coded majority component value
flattened_1 = [evecs[1][0]*data[0,:], evecs[1][1]*data[0,:]]

ax1 = plt.gca()
#set1 = ax1.plot(flattened_0[0], flattened_0[1], "rx", label="PCA 0")
set2 = ax1.plot(flattened_1[0], flattened_1[1], "gx", label="PCA 1")
ax1.set_aspect('equal', adjustable='box')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("PCA Analysis of Weight vs Height")
plt.legend(loc='upper left')
plt.savefig("PCA_result.png")