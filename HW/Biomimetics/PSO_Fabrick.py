# Particle Swarm Optimization Algorithm
# By: Noah Fabrick

import numpy as np
import random as rd

class Particle:

    def __init__(self,x,v,w,phi_p,phi_g):
        self.x = x
        self.v = v
        self.w = w
        self.phi_p = phi_p
        self.phi_g = phi_g

    def updatePos(self):
        self.x = self.x + self.v
    
    def updateVel(self):
        randP = rd.uniform(0,1)
        randG = rd.uniform(0,1)
        self.v = self.v + randP + randG

    def updateValue(self):
        pass

def ackley3D(x):
    a = 20
    b = 0.2
    c = 2*np.pi
    d = len(x)

    sum1 = 0
    sum2 = 0
    for i in range(d):
        sum1 += x[i]**2
        sum2 += np.cos(c*x[i])
    
    term1 = -a+np.exp(-b*np.sqrt(sum1/d))
    term2 = -1*np.exp(sum2/d)

    return term1+term2+a+np.exp(1)