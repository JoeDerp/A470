# Ant Colony Optimization applied to Travelling Sales-Ant Problem
# By: Noah Fabrick

import numpy as np
import random as rd

# Step 1 - Initialization
tau = np.ones((5,5))
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

def probability(tau,eta,r,s):
    probs = []
    a = 1
    b = 2
    for i in range(len(s)):
        p_rs = tau[r-1][s[i]-1]**a*eta[r-1][s[i]-1]**b
        probs.append(p_rs)
    return probs

def chooseNode(probs, s):
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
    val = 0
    for i in range(1,len(path)):
        val += d[path[i-1]-1][path[i]-1]
    return val

def addPher(path,value,tau):
    pher = np.zeros((5,5))
    delTau = 1/value
    for i in range(1,len(path)):
        pher[path[i-1]-1][path[i]-1] = delTau
    # If evap tau
    newTau = 0.5*tau + pher
    return newTau
    # If evap ones
    # newTau = 0.5*np.ones((5,5)) + pher
    # return newTau


# Test
# s = [1,2,3,4,5]
# r = 1
# s.remove(r)
# eta = visMat(d,r)
# probs = probability(tau,eta,r,s)
# new_r = chooseNode(probs,s)

s = [1,2,3,4,5]
r = rd.choice(s)
path = [r]
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
tau = addPher(path,val,tau)


print(calcVal([1,4,3,5,2,1],d))
newTau = addPher([1,4,2,5,3,1],60,np.ones((5,5)))
print(newTau)