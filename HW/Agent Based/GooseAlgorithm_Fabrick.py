import GooseModule as gse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import *
#from vpython import *

# Intialization
numGeese = 20
a = 1
ch = 0.5
rField = [-numGeese,numGeese]
geese = gse.Geese(numGeese,a,ch,rField)

fig1, ax1 = plt.subplots()
for g in geese.pop:
    ax1.plot(g.x[0],g.x[1],'b^')
    ax1.add_artist(plt.Circle((g.x[0], g.x[1]), g.d_nom, color='r', linestyle=':', fill=False))
ax1.xlim = (rField[0],rField[1])
ax1.ylim = (rField[0],rField[1])
ax1.set_title('Initial Geese Positions')
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
ax1.grid(True)

# Simulation
fig2, ax2 = plt.subplots()
# Step 5: Implement the Animation
geese.findLeads()
dx = 0.1
time = 1000

def animate(step):
    ax2.clear()
    geese.rHat()
    geese.updatePos(dx)
    for goose in geese.pop:
        ax2.plot(goose.x[0], goose.x[1], 'b^')
    yMax = geese.pop[geese.popLead].x[1]
    ax2.set_xlim(rField[0], rField[1])
    ax2.set_ylim(yMax-(rField[1]-rField[0]), yMax+5)
    ax2.set_title(f'Geese Positions over Time, t = {step}')
    ax2.set_ylabel('Y')
    ax2.set_xlabel('X')
    ax2.grid(True)

# Create the animation
ani = FuncAnimation(fig2, animate, frames=1000, interval=20)

plt.show()

# t = 10000 # number of seconds to run the flight simulation for
# dx = 0.1 # geese travel at 0.1 units/s
# geese.findLeads()
# for i in range(t):
#     geese.rHat()
#     geese.updatePos(dx)
#     for g in geese.pop:
#         plt.plot(g.x[0],g.x[1],'b^')
#     plt.show()

# fig2, ax2 = plt.subplots()
# for g in geese.pop:
#     ax2.plot(g.x[0],g.x[1],'b^')
# ax2.set_title('Final Geese Positions')
# ax2.set_ylabel('Y')
# ax2.set_xlabel('X')
# ax2.grid(True)
# plt.show()

# Create geese objects in VPython
# geese_spheres = [sphere(pos=vector(goose.x[0],goose.x[1],0), radius=a) for goose in geese.pop]

# # Run the simulation
# dx = 0.1
# geese.findLeads()
# while True:
#     rate(1)  # Set the frame rate
#     geese.rHat()
#     geese.updatePos(dx)
#     for goose, sphere_obj in zip(geese.pop, geese_spheres):
#         sphere_obj.pos = goose.pos
