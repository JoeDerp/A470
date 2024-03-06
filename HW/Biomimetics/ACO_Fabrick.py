# Ant Colony Optimization applied to Travelling Sales-Ant Problem
# By: Noah Fabrick

import numpy as np
import random as rd
import matplotlib.pyplot as plt

def visMat(d,r):
    # Create intial visibility matrix, eta = 1/d
    eta = d.astype(float)
    for i in range(len(eta)):
        eta[i][r-1] = 0
        for j in range(len(eta[0])):
            if j != r-1:
                if eta[i][j] != 0:
                    eta[i][j] = 1/eta[i][j]
    return eta

def probability(tau,eta,r,s):
    # Calculate probabilites of each neighboor, p_rs = tau(r,s)^a*eta(r,s)^b
    probs = []
    a = 1
    b = 2
    for i in range(len(s)):
        p_rs = tau[r-1][s[i]-1]**a*eta[r-1][s[i]-1]**b
        probs.append(p_rs)
    return probs

def chooseNode(probs, s):
    # Choose next r from random selection from s probabilities
    sumMk = sum(probs)
    probsL = [p_rs/sumMk for p_rs in probs] # Generate local probabilities
    # Generate cumulative probabilities
    probsC = []
    for i in range(len(probsL)):
        if i == 0:
            probsC.append(probsL[i])
        else:
            probsC.append(probsL[i]+probsC[i-1])
    randS = rd.random() # Random decimal on [0,1)
    for new_r in s:
        if randS < probsC[s.index(new_r)]:
            return new_r

def calcVal(path,d):
    # Calculate distance traveled value given ant path
    val = 0
    for i in range(1,len(path)):
        val += d[path[i-1]-1][path[i]-1]
    return val

def addPher(path,value):
    # Create update pheremone matrix from path values
    pher = np.zeros((5,5))
    delTau = 1/value
    for i in range(1,len(path)):
        pher[path[i-1]-1][path[i]-1] = delTau
    return pher



# Problem Initialization
tau = np.ones((5,5))
d = np.array([[0,10,12,11,14],[10,0,13,15,8],[12,13,0,9,14],[11,15,9,0,16],[14,8,14,16,0]])
s0 = [1,2,3,4,5]
numAnts = 3
iterations = 50
sols = []

for i in range(iterations):
    sol_i = []
    phers = np.zeros((5,5))
    for i in range(1,numAnts+1):
        r = rd.choice(s0)
        path = [r]
        s = s0.copy()
        s.remove(r)
        eta = visMat(d,r)
        for i in range(4):
            probs = probability(tau,eta,r,s)
            r = chooseNode(probs,s)
            path.append(r)
            s.remove(r)
            for j in range(len(eta)):
                eta[j][r-1] = 0
        path.append(path[0])
        val = calcVal(path,d)
        phers += addPher(path,val)
        sol_i.append((path,val))
    tau = 0.5*tau + phers
    sols.append(sol_i)


print('The best path found was',sols[len(sols)-1][0][0],' with a distance value of',sols[len(sols)-1][0][1])
# Best answer: Some sequence in the order of 1 -> 4 -> 3 -> 5 -> 2 -> 1 , with a value of 52

avgVals = [(s[0][1]+s[1][1]+s[2][1])/3 for s in sols]
iters = [i for i in range(1,iterations+1)]
fig, ax = plt.subplots()
ax.plot(iters,avgVals)
ax.set_title('Average Path Distance of One Ant at each Iteration')
ax.set_ylabel('Average Path Distance')
ax.set_xlabel('Iteration')
ax.grid(True)
plt.show()