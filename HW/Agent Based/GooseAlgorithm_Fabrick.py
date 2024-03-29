import GooseModule as gse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, HTMLWriter
from matplotlib.animation import FFMpegWriter
from vpython import *

# Intialization
numGeese = 20
a = 1
ch = 0.5
rField = [-numGeese,numGeese]
geese = gse.Geese(numGeese,a,ch,rField)

'''
# Create plot showing geese initial positions
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
'''

# VPython Visualization
# Create a sphere in vpython for every goose
geese_bodies = [sphere(pos=vector(goose.x[0],goose.x[1],0), radius=a) for goose in geese.pop]
# Set Camera FOV
scene.range = numGeese
# Create Background Grid
scene.xaxis = cylinder(pos=vector(-50,  0, 0), axis=vector(100, 0, 0), radius=0.05, color=color.green)
scene.xaxis = cylinder(pos=vector(-50, 25, 0), axis=vector(100, 0, 0), radius=0.05, color=color.green)
scene.xaxis = cylinder(pos=vector(-50, 50, 0), axis=vector(100, 0, 0), radius=0.05, color=color.green)
scene.xaxis = cylinder(pos=vector(-50, 75, 0), axis=vector(100, 0, 0), radius=0.05, color=color.green)
scene.xaxis = cylinder(pos=vector(-50,100, 0), axis=vector(100, 0, 0), radius=0.05, color=color.green)
scene.yaxis = cylinder(pos=vector(0, -10, 0), axis=vector(0, 110, 0), radius=0.05, color=color.green)

# Run the simulation
geese.findLeads()
dx = 0.1
time = 1000
t = 0
while t < time:
    rate(30)
    geese.rHat()
    geese.updatePos(dx)
    for goose, body in zip(geese.pop, geese_bodies):
        body.pos = vector(goose.x[0],goose.x[1],0)
    scene.center = vector(0,geese.pop[geese.popLead].x[1]-10,0)
    t += 1

'''
# Matplotlib Visualization
fig2, ax2 = plt.subplots()
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
writer = HTMLWriter()
ani.save(filename="\\geese.html", writer=writer)
'''