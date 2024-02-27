import numpy as np
import random as rd
d = np.array([[0,10,12,11,14],[10,0,13,15,8],[12,13,0,9,14],[11,15,9,0,16],[14,8,14,16,0]])

# Step 2 - Visibility Matrix and Probabilities

# Updaate Pheremone Matrix


def visMat(d,r):
    eta = d.astype(float)
    for i in range(len(eta)):
        eta[i][r-1] = 0
        for j in range(len(eta[0])):
            if j != r-1:
                if eta[i][j] != 0:
                    eta[i][j] = 1/eta[i][j]
    return eta

r = 1
eta = visMat(d,r)
r = 3
for j in range(len(eta)):
    eta[j][r-1] = 0
print(eta)
tau = np.ones((5,5))
print(tau)
print(tau*0.5)
tau += visMat(d,r)
print(tau)