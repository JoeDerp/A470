# Particle Swarm Optimization to solve Ackley Function
# By: Noah Fabrick

import PSO_Fabrick as pso
import numpy as np
import matplotlib.pyplot as plt

# Commented out plot code is for visualization of particle swarm with 50 iterations
# fig1,ax1 = plt.subplots()
# ax1.set_title('Intial Random Particle Positions')
# ax1.set_ylabel('$x_2$')
# ax1.set_xlabel('$x_1$')
# ax1.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)

# Initialization
S = 20 # number of particles
d = 3 # number of dimensions
g = np.random.uniform(-32.768,32.768,d) # random guess at g within bounds
particles = []
for s in range(S):
    x = np.random.uniform(-32.768,32.768,d) # initialize 3D position from uniform distribution on domain
    # ax1.plot(x[0],x[1],'b*')
    v = np.random.uniform(-np.abs(32.768-(-32.768)),np.abs(32.768-(-32.768)),d) # initialize velocity from distribution with bounds
    particles.append(pso.Particle(x,v,0.8,0.1,0.1)) # create particle
    particles[s].p = x # make random initial position best known particle position
    if pso.ackley3D(x) < pso.ackley3D(g): # update global best position if f(x)=f(p) beats f(g)
        g = x

# fig2,ax2 = plt.subplots()
# ax2.set_title('Particle Positions at n = 10')
# ax2.set_ylabel('$x_2$')
# ax2.set_xlabel('$x_1$')
# ax2.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)
# fig3,ax3 = plt.subplots()
# ax3.set_title('Particle Positions at n = 20')
# ax3.set_ylabel('$x_2$')
# ax3.set_xlabel('$x_1$')
# ax3.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)
# fig4,ax4 = plt.subplots()
# ax4.set_title('Particle Positions at n = 30')
# ax4.set_ylabel('$x_2$')
# ax4.set_xlabel('$x_1$')
# ax4.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)
# fig5,ax5 = plt.subplots()
# ax5.set_title('Particle Positions at n = 40')
# ax5.set_ylabel('$x_2$')
# ax5.set_xlabel('$x_1$')
# ax5.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)
# fig6,ax6 = plt.subplots()
# ax6.set_title('Particle Positions at n = 50')
# ax6.set_ylabel('$x_2$')
# ax6.set_xlabel('$x_1$')
# ax6.grid(True)
# plt.xlim(-32.768,32.768)
# plt.ylim(-32.768,32.768)

# Swarm
n = 0
nIter = 50 # number of iterations
part: pso.Particle
while n < nIter:
    for part in particles:
        part.updateVel(g) # update particle velocity based on best known value globally
        part.updatePos() # update particle pasition based on velocity
        part.p, g = part.updateValue(pso.ackley3D,g) # update best known particle and global value
        # if n == 9:
        #     ax2.plot(part.x[0],part.x[1],'b*')
        # elif n == 19:
        #     ax3.plot(part.x[0],part.x[1],'b*')
        # elif n == 29:
        #     ax4.plot(part.x[0],part.x[1],'b*')
        # elif n == 39:
        #     ax5.plot(part.x[0],part.x[1],'b*')
        # elif n == 49:
        #     ax6.plot(part.x[0],part.x[1],'b*')
    n += 1

print('Estimated global minimum of:',g,'with',S,'particles in',nIter,'iterations')
# Estimated global minimum of: [-0.10506389  0.10180948  0.14258471] with 20 particles in 50 iterations