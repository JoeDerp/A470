import GooseModule as gse
import numpy as np
import matplotlib.pyplot as plt

# Intialization
numGeese = 8
a = 1
ch = 0.5
geese = gse.Geese(numGeese,a,ch)

fig1, ax1 = plt.subplots()
for g in geese.pop:
    ax1.plot(g.x[0],g.x[1],'b^')
    ax1.add_artist(plt.Circle((g.x[0], g.x[1]), g.d_nom, color='r', linestyle=':', fill=False))
ax1.xlim = (0,2*numGeese)
ax1.ylim = (0,2*numGeese)

geese.findLead()
ax1.add_artist(plt.Rectangle((geese.pop[geese.global_i].x[0]-a, geese.pop[geese.global_i].x[1]-(ch/2)), 2*a, ch, color='g', fill=True))
geese.rHats()

# Flight

for i in range(1000):
    dt = 0.1
    geese.updatePos(dt)
    geese.findLead()
    geese.rHats()

fig2, ax2 = plt.subplots()
for g in geese.pop:
    ax2.plot(g.x[0],g.x[1],'b^')
plt.show()
# geese = []
# for g in range(numGeese):
#     xRand = np.random.uniform(0,numGeese*2,2)
#     plt.plot(xRand[0],xRand[1],'b^')
#     plt.xlim(0,2*numGeese)
#     plt.ylim(0,2*numGeese)
#     geese.append(gse.Goose(xRand,a,ch))
#     plt.gca().add_artist(plt.Circle((geese[g].x[0], geese[g].x[1]), geese[g].d_nom, color='r', fill=False))

# # Simulation
# goose: gse.Goose
# for goose in geese:
#     goose.findLead(geese)


# plt.gca().add_artist(plt.Rectangle((geese[5].x[0]-a, geese[5].x[1]-(ch/2)), 2*a, ch, color='g', fill=True))
# plt.show()
