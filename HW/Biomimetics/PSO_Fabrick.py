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
        for i in range(len(self.x)):
            self.x[i] = self.x[i]+self.v[i]
        return self
    
    def updateVel(self,g):
        rP = rd.uniform(0,1)
        rG = rd.uniform(0,1)
        for i in range(len(self.v)):
            self.v[i] = self.w*self.v[i] + self.phi_p*rP*(self.p[i]-self.x[i]) + self.phi_g*rG*(g[i]-self.x[i]) 
        return self

    def updateValue(self,func,g):
        if func(self.x) < func(self.p):
            self.p = self.x
        if func(self.p) < func(g):
            g = self.p
        return self.p,g

def f(x):
    return ((x[0]-3.14)**2+(x[1]-2.72)**2+np.sin(3*x[0]+1.41)+np.sin(4*x[1]-1.73))

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

# part = Particle([0.,0.,0.],[1.,2.,-1.],0.8,0.1,0.1)
# part.updatePos()
# print(part.x)
# part.updatePos()
# print(part.x)
# part.p = part.x
# part.updateVel([0,0,0])
# print(part.v)
# part.updatePos()
# print(part.x)