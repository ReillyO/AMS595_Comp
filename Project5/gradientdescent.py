######################################
#        Gradient Descent            #
######################################

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# void callback function to be passed into the minimization function
# will store the iteration's loss values and x array in the global
# verbose variable, return nothing
def callback_func(intermediate_result):
    global verbose
    verbose = np.append(verbose, intermediate_result)
    return

A = np.random.rand(5000) # 1D version of 100x50 "target" matrix
print(A)

loss_func = lambda X : 0.5 * sum((X-A) ** 2)

verbose = np.array([]) # container for mid-minimization stat output

X = np.random.rand(5000) # Initial random guess 

#print(loss_func(X)) # sanity check

# main minimization, goes until loss function dips below tolerance and output
# loss values to callback function at every iteration
result = sp.optimize.minimize(loss_func, X, tol=1e-6, callback=callback_func) 
X_final = np.split(result["x"], 50)  # regenerate 100x50 array

loss_vals = np.array([])

# extract loss values at each iteration from callback output
for entry in verbose:
    loss_vals = np.append(loss_vals, entry["fun"])

# debug
print("LOSS VALUES: ",loss_vals)

# set up ticks for x axis
x_ticks = np.linspace(0, len(loss_vals), len(loss_vals))

# plot progression of loss value over iterations of minimization
plt.plot(x_ticks, loss_vals, "b-")
plt.xlabel("Iteration")
plt.ylabel("Loss Function Value")
plt.title("Loss Function vs Minimization Iteration")
plt.savefig("lossvals.png")

#print(X_final)