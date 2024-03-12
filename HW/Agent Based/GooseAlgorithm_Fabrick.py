import GooseModule as gse
import numpy as np
import matplotlib.pyplot as plt

# Intialization
numGeese = 10
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
t = 10000 # number of seconds to run the flight simulation for
dx = 0.1 # geese travel at 0.1 units/s
geese.findLeads()
for i in range(t):
    geese.rHat()
    geese.updatePos(dx)

fig2, ax2 = plt.subplots()
for g in geese.pop:
    ax2.plot(g.x[0],g.x[1],'b^')
ax2.set_title('Final Geese Positions')
ax2.set_ylabel('Y')
ax2.set_xlabel('X')
ax2.grid(True)
plt.show()
