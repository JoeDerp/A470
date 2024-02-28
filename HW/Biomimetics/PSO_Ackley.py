# Particle Swarm Optimization to solve Ackley Function
# By: Noah Fabrick

import PSO_Fabrick as pso
import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(-32.768,32.768)

y = pso.ackley3D([xi,xi])

print(y)

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# ax.plot_surface(xi,xi,y,cmap='viridis')