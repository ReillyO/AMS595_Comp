####################################################
#         mandelbrot.py                            #
####################################################
import numpy as np
import matplotlib.pyplot as plt

# Method to check if a given complex number converges or diverges based on Mandelbrot relation
# -1 if converges, iteration count at divergence if diverges
def check_convergence(complex_val):
    NMAX = 100
    THRESHOLD = 50
    z = complex_val
    for i in range(NMAX):
        if abs(z) > THRESHOLD:
            return i
        z = z**2 + complex_val
    return -1
        


# create grid
GRIDSIZE=500
x, y = np.mgrid[-2:1:500j, -1.5:1.5:500j]
c_grid = x + 1j*y

# initialize mandelbrot mask grid as zeros
mandelbrot_mask = np.zeros(shape=(GRIDSIZE,GRIDSIZE))

# for every complex number in the grid, use custom function to determine convergence
# and store associated value in mandelbrot_mask
for i in range(c_grid.shape[0]):
    for j in range(c_grid.shape[1]):
        mandelbrot_mask[i][j] = check_convergence(c_grid[i][j])

# If the mask has -1 at any index to indicate convergence, change value to 100 for pure white
mandelbrot_mask = np.where(mandelbrot_mask > 0, mandelbrot_mask, 100)

# Generate image of the fractal using the mandelbrot_mask and save
plt.imshow(mandelbrot_mask.T, extent=[-2,1,-1.5,1.5])
plt.gray()
plt.title("Mandelbrot Fractal")
plt.savefig('mandelbrot.png')
plt.show()