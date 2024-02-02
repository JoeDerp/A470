# HW1 : Stochastic Methods
# By : Noah Fabrick


import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt

# Problem 1

def monteCarloPi(r,N):
    '''
    N is number of trials
    pythagoras -> x^2+y^2=r^2
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

# r = 2
# N = 1000
# piHat,xHat,yHat = monteCarloPi(r,N)
# print("PI ~=", piHat)

# # Plot points on a scatter plot, blue if out of r, green if within r
# fig1, ax1 = plt.subplots()
# for i in range(N):
#     if xHat[i]**2 + yHat[i]**2 <= r**2:
#         ax1.scatter(xHat[i],yHat[i],None,'b')
#     else:
#         ax1.scatter(xHat[i],yHat[i],None,'g')

# # Create unit circle with radius r using numpy
# theta = np.linspace(0,np.pi/2)
# yCirc = r*np.sin(theta)
# xCirc = r*np.cos(theta)
# ax1.plot(xCirc,yCirc,color='r')
# ax1.set_title('Monte Carlo Estimation of Pi')
# ax1.set_ylabel('Y')
# ax1.set_xlabel('X')
# ax1.grid(True)


# Problem 2

def monteCarloMVT_Integral(func, xMin, xMax, N):
    sum = 0
    for i in range(N):
        xHat = random.uniform(xMin,xMax)
        sum += func(xHat)
    return ((xMax-xMin)*sum)/N

func = lambda x : x**3*np.sin(x)
xMin = -2
xMax = 3
trueVal = 15.66464985
absTol = 1
N = 0
while absTol > 0.001:
    N += 10
    mcVal = monteCarloMVT_Integral(func, xMin, xMax, N)
    absTol = abs(trueVal-mcVal)

print(monteCarloMVT_Integral(func,-2,3,10000))
print(mcVal,"in",N)