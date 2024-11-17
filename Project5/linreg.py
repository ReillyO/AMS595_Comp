######################################
#        Least Squares Linreg        #
######################################
import numpy as np
import scipy as sp

house_features = np.array([[2100, 3, 20],
                           [2500, 4, 15],
                           [1800, 2, 30],
                           [2200, 3, 25]]) 
house_prices = np.array([460, 540, 330, 400])

lstsq, residues, rank, s = sp.linalg.lstsq(house_features, house_prices)

# use to predict

new_house = [2400, 3, 20]

# this is really screwy for some reason?
new_house_price = round(np.matmul(lstsq, new_house), 4)
print(f"LEAST SQUARES SOLUTION\nHouse with \nSquare Footage: {new_house[0]}\nBathrooms: {new_house[1]}\nYears old: {new_house[2]}\nPredicted Cost: ${new_house_price}\n")

# compare to linalg.solve() which requires a square matrix
direct_solve = sp.linalg.solve(house_features[0:3], house_prices[0:3])
print(f"Least Squares solution: {lstsq}")
print(f"Direct solution: {direct_solve}\n")
new_house_price = round(np.matmul(direct_solve, new_house), 4)
print(f"DIRECT SOLUTION\nHouse with \nSquare Footage: {new_house[0]}\nBathrooms: {new_house[1]}\nYears old: {new_house[2]}\nPredicted Cost: ${new_house_price}\n")

# both solve reasonably but least-squares allows for the consideration of more data at
# the danger of overfitting the prediction