# HW1 : Stochastic Methods
# By : Noah Fabrick

import random
import numpy as np
import matplotlib.pyplot as plt

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

r = 1
absTol = 1
N = 0
while absTol > 0.031416: # Within 1% of Pi -> absTol = pi*0.01 = 0.031416
    N += 10
    pi0,xHat,yHat = monteCarloPi(r,N)
    absTol = abs(pi0 - np.pi)
print('Problem 1')   
print("Monte Carlo method estimated Pi to be", pi0,"in",N,"iterations at",(absTol/np.pi)*100,"% away from numpy's Pi.")

# Plot points on a scatter plot, blue if out of r, green if within r
fig1, ax1 = plt.subplots()
for i in range(N):
    if xHat[i]**2 + yHat[i]**2 <= r**2:
        ax1.scatter(xHat[i],yHat[i],None,'b')
    else:
        ax1.scatter(xHat[i],yHat[i],None,'g')

# Create unit circle with radius r using numpy
theta = np.linspace(0,np.pi/2)
yCirc = r*np.sin(theta)
xCirc = r*np.cos(theta)
ax1.plot(xCirc,yCirc,color='r')
ax1.set_title('Monte Carlo Estimation of Pi')
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
ax1.grid(True)

# Problem 2

def monteCarloMVT_Integral(func, xMin, xMax, N):
    sum = 0 # sum of f(xHat)
    for i in range(N):
        xHat = random.uniform(xMin,xMax)
        sum += func(xHat)
    return ((xMax-xMin)*sum)/N # E_N = (b-a)*sum(f(xHat))/N

# Estimate int(x^3*sin(x))|-2 to 3
func = lambda x : x**3*np.sin(x)
xMin = -2
xMax = 3
trueVal = 15.66464985 # true solution from symbolab
# Add to number of iterations until estimated value is within absolute tolerance
absTol0 = 1
N_0 = 1
absTols = []
Ns = []
vals = []
while absTol0 > 0.001:
    Ns.append(N_0)
    mcVal = monteCarloMVT_Integral(func, xMin, xMax, N_0)
    absTol0 = abs(trueVal-mcVal)
    vals.append(mcVal)
    absTols.append(absTol0)
    N_0 += 10
    
fig2, (ax2a, ax2b) = plt.subplots(2,1)
ax2a.plot(Ns,vals)
ax2b.plot(Ns,absTols)
ax2a.set_title('Monte Carlo Estimation of Integral')
ax2a.set_ylabel('Estimated Integral Value]')
ax2b.set_ylabel('Absolute Error')
ax2b.set_xlabel('Number of Iterations')
ax2a.grid(True)
ax2b.grid(True)

print("Problem 2")
print("Calulated", mcVal,"with",N_0,"monte carlo iterations at an absolute tolerance of",absTol0)

# Problem 3

def monteCarloGasLaw(P0, T0, pErr, tErr, rGas, N):

    rho0 = P0/(rGas*(T0+273.15))
    sum = 0
    for i in range(N):
        T_Hat = random.normalvariate(T0,tErr) + 273.15 # convert to K
        pHat = random.normalvariate(P0,pErr)
        sum += pHat/T_Hat
    rhoHat = sum/(rGas*N)
    rhoErr = abs(rho0-rhoHat)
    return rhoHat, rho0, rhoErr

# Approximate density with P = 104847 +/- 52
P0 = 104847 # Pa
pErr = 52
T0 = 25 # deg C
tErr = 0.2
rGas = 287.053 # J/kg*K
N3 = 1
rhoHat, rho0, rhoErr = monteCarloGasLaw(P0, T0, pErr, tErr, rGas, N3)
rhoMax = (P0+pErr)/(rGas*(T0+tErr+273.15))
rhoAbs = abs(rho0-rhoMax)
print("Problem 3")
print("For pressure reading with a standard deviation of 52:\n","Zero Error --> air density =",rho0,"and absolute error =",0,'\n',"Monte Carlo Error with",N3,"iterations --> air density =",rhoHat,"and absolute error =",rhoErr,'\n',"Error at 1 Standard Deviation --> air density =",rhoMax,"and absolute error =",rhoAbs)

# Approximate density with P error = 0:50:800
pErrs = []
rhoErrs = []
pErr0 = 0
for i in range(16):
    NaN, NaN, rhoErr0 = monteCarloGasLaw(P0,T0,pErr0,tErr,rGas,1)
    pErr0 += 50
    pErrs.append(pErr0)
    rhoErrs.append(rhoErr0)
fig3, ax3 = plt.subplots()
ax3.plot(pErrs,rhoErrs)
ax3.set_title('Monte Carlo Estimation of Air Density with Ideal Gas Law')
ax3.set_ylabel('Absolute Error in Density [kg/m^3]')
ax3.set_xlabel('Absolute Error in Pressure [Pa]')
ax3.grid(True)

# Problem 4

def monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,N):
    '''
    Given (min, mode, max) from each input variable
    Randomly generates value from triangle distribution for each input N times
    Calculates projected earnings from each iteration of random value generation
    '''
    unitPriceHat = np.random.default_rng().triangular(unitPrice[0],unitPrice[1],unitPrice[2],N)
    unitSalesHat = np.random.default_rng().triangular(unitSales[0],unitSales[1],unitSales[2],N)
    varCostHat = np.random.default_rng().triangular(varCost[0],varCost[1],varCost[2],N)
    fixedCostHat = np.random.default_rng().triangular(fixedCost[0],fixedCost[1],fixedCost[2],N)
    earnings = []
    for i in range(N):
        # earning = (unit price) × (unit costs) − (variable costs + fixed costs)
        earnings.append(unitPriceHat[i]*unitSalesHat[i] - (varCostHat[i]+fixedCostHat[i]))
    
    xHat = np.mean(earnings) # estimated mean
    sigHat = np.std(earnings) # estimated standard deviation
    
    return earnings, xHat, sigHat

# (min val, mode, max val) given for each input
unitPrice = (50,55,70)
unitSales = (2000,2440,3000)
varCost = (50000,55200,65000)
fixedCost = (10000,14000,20000)
# run profit estimation with N = 10,000 iterations
earnings1, mean1, std1 = monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,10000)

# 95% confidence interval
earnings2, mean2, std2 = monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,100) # pilot -> n = 100
zScore = 1.96
mu = 1000
n95 = (std2**2*zScore**2)/mu**2
earnings3, mean3, std3 = monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,int(n95))
ci = [mean3 - zScore*(std3/n95**0.5),mean3 + zScore*(std3/n95**0.5)]

print("Problem 4")
print("95% Confidence Interval of",ci,"with a range of",ci[1]-ci[0],"dollars")

#plot histogram of generated earnings
fig4, ax4 = plt.subplots()
ax4.hist(earnings1,bins=15)
ax4.set_title('Computed Earnings from 10,000 Monte Carlo Runs',)
ax4.set_ylabel('# of Occurences')
ax4.set_xlabel('Computed Earnings [$]')
ax4.grid(True)
plt.show()