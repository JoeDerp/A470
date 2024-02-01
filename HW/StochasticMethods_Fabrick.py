# HW1 : Stochastic Methods
# By : Noah Fabrick


import random
import matplotlib as mlt
import matplotlib.pyplot as plt

def monteCarloPi(r,N):
    '''
    N is number of trials
    Eqn. of circle -> x^2+y^2=r^2
    Area for quarter circle -> A_c = (PI*r^2)/4
    Area for square -> A_s = r^2
    To estimate pi use -> PI = 4*(A_c/A_s)
    with A_c = num of generated points <= r , A_s = total generated points , x and y random between (0, r)
    '''
    areaSquare = 0 # number of generated points
    areaCircle = 0 # number of points within radius
    xHat = []
    yHat = []
    for i in range(N):
        areaSquare += 1
        xHat.append(random.uniform(0,r))
        yHat.append(random.uniform(0,r))
        if xHat[i]**2 + yHat[i]**2 <= r**2:
            # count if generated point is <= r
            areaCircle += 1
    piHat = (areaCircle/areaSquare)*4

    return piHat,xHat,yHat

r = 1
N = 1000
piHat,xHat,yHat = monteCarloPi(r,N)
print("PI ~=", piHat)
plt.scatter(xHat,yHat)

# for i in N:
#     if xHat(i)**2 + yHat(i)**2 <= r**2:
#         plt.scatter(xHat,yHat)