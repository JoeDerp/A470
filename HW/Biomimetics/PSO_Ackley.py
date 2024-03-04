# Particle Swarm Optimization to solve Ackley Function
# By: Noah Fabrick

import PSO_Fabrick as pso
import numpy as np
import matplotlib.pyplot as plt

# # Initialize
# S = 20 # number of particles
# g = [0,0] 
# particles = []
# for s in range(S):
#     x = np.random.uniform(0,5,2) # initialize position from uniform distribution on domain
#     v = np.random.uniform(-np.abs(5-0),np.abs(5-0),2) # initialize velocity from distribution
#     particles.append(pso.Particle(x,v,0.8,0.1,0.1)) # create particle
#     particles[s].p = x # make random initial position best known particle position
#     if pso.f(x) < pso.f(g): # update global best position if f(x)=f(p) beats f(g)
#         g = x

# # Swarm
# n = 0
# part: pso.Particle
# while n < 50:
#     for part in particles:
#         part.updateVel(g)
#         part.updatePos()
#         part.p, g = part.updateValue(pso.f,g)
#         plt.plot(part.x[0],part.x[1],'b*')
#         n += 1
# plt.show()

# Initialize
S = 20 # number of particles
g = [0,0,0] 
particles = []
for s in range(S):
    x = np.random.uniform(-32.768,32.768,3) # initialize 3D position from uniform distribution on domain
    v = np.random.uniform(-np.abs(32.768-(-32.768)),np.abs(32.768-(-32.768)),3) # initialize velocity from distribution
    particles.append(pso.Particle(x,v,0.8,0.1,0.1)) # create particle
    particles[s].p = x # make random initial position best known particle position
    if pso.ackley3D(x) < pso.ackley3D(g): # update global best position if f(x)=f(p) beats f(g)
        g = x

# Swarm
n = 0
part: pso.Particle
while n < 50:
    for part in particles:
        part.updateVel(g)
        part.updatePos()
        part.p, g = part.updateValue(pso.ackley3D,g)
        n += 1