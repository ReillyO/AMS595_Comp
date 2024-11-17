###########################################
#             taylor_series.py            #
###########################################
import sympy as sp
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from math import factorial as fact

START, END, POINTS, C = -10.0, 10.0, 100, 0
INIT_DEG, TERM_DEG, STEP_DEG = 50, 100, 5

# Calculation of Taylor function at given $fixed_c in range [$start, $end]
# Will:
#   - Calculate an approximation of any given function in Taylor form
#     to $degree polynomial degrees and store in $f_x
#   - Use this generated function to calculate 100 points along the interval
#     given by [$start, $end]
# Returns:
#   - Pandas Series of 100 points provided by the Taylor approximation
def taylor_at_point(func, start, end, degree, fixed_c):
    NPOINTS = 100
    x = sp.symbols("x")
    f_x = 0
    approx_points = pd.Series(np.zeros(NPOINTS))
    # generate Taylor polynomial and store symbolic in f_x
    for n in range(degree):
        tmp_func = sp.diff(func, x, n)
        f_x += (tmp_func.subs(x, fixed_c)/fact(n)).evalf() * (x - fixed_c)**n
    count = 0
    steps = np.linspace(start, end, NPOINTS)
    # generate 100 points using the Taylor approximation
    for x_val in steps:
        approx_points[count] = float(f_x.subs(x, x_val))
        count += 1
    return approx_points

# Benchmarking of Taylor approximation efficiency
# Will:
#   - Calculate a Taylor approximation for every m provided in the linear space
#     [$initial_deg, $final_deg, $deg_step]
#   - Record the times and summed error of the returned approximation points
# Returns:
#   - Pandas Dataframe containing columns for the degree, time for calculation, and 
#     error of each Taylor approximation
def taylor_in_range(func, start, end, degree, fixed_c, initial_deg, final_deg, deg_step):
    # initialize empty arrays and count
    degree_linspace = range(initial_deg, final_deg, deg_step)
    degrees = pd.Series(np.zeros(len(degree_linspace)))
    times = pd.Series(np.zeros(len(degree_linspace)))
    errors = pd.Series(np.zeros(len(degree_linspace)))
    count = 0
    # for every degree provided along the step, get a Taylopr approximation and
    # record the time it took as well as the error of the final points
    for degree in degree_linspace:
        tic = time.time()
        exp_points = taylor_at_point(func, start, end, degree, fixed_c)
        ref_points = pd.Series(np.zeros(len(degree_linspace)))
        x_vals = np.linspace(START, END, POINTS)
        for i in range(ref_y.size):
            ref_points[i] = float(func.subs(x, x_vals[i]))
        toc = time.time()
        # print(exp_points) # debug
        tmp_error = sum(abs(exp_points - ref_points))
        tmp_time = toc - tic
        degrees[count] = degree
        times[count] = tmp_time
        errors[count] = tmp_error
        count += 1
    # create the return array and return it
    return_array = pd.concat([degrees, times, errors], axis=1)
    return_array.columns = ["Degree", "Time (s)", "Error"]
    return return_array

######### PART 1 ##########

x_vals = np.linspace(START, END, POINTS)

x = sp.symbols("x")
sample_f = x * (sp.sin(x))**2 + sp.cos(x)
taylor_y = taylor_at_point(sample_f, START, END, POINTS, C)
# taylor_y = ref_y = pd.Series(np.zeros(POINTS)) # debug
ref_y = pd.Series(np.zeros(POINTS))
for i in range(ref_y.size):
    ref_y[i] = float(sample_f.subs(x, x_vals[i]))

# plot approx points
plt.plot(x_vals, taylor_y, 'ro', label="Taylor Approximation")
plt.plot(x_vals, ref_y, 'k-', label="Actual")
plt.xlabel("x")
plt.ylabel("xsin(x)^2 + cos(x)")
plt.legend(loc='best')
plt.savefig("Taylor_Approx.png")

########## PART 2 ##########

benchmark = taylor_in_range(sample_f, START, END, POINTS, C, INIT_DEG, TERM_DEG, STEP_DEG)
# print(benchmark) # debug
benchmark.to_csv("taylor_approx_benchmark.csv", index=False)