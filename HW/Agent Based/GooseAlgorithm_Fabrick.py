import GooseModule as gse
import numpy as np
import matplotlib.pyplot as plt

# Intialization
numGeese = 20
a = 1
ch = 0.5
geese = []
for g in range(numGeese):
    xRand = np.random.uniform(0,numGeese*2,2)
    plt.plot(xRand[0],xRand[1],'b^')
    plt.xlim(0,2*numGeese)
    plt.ylim(0,2*numGeese)
    geese.append(gse.Goose(xRand,a,ch))
    plt.gca().add_artist(plt.Circle((geese[g].x[0], geese[g].x[1]), geese[g].d_nom, color='r', fill=False))

# Simulation
goose: gse.Goose
for goose in geese:
    goose.findLead(geese)


plt.gca().add_artist(plt.Rectangle((geese[5].x[0]-a, geese[5].x[1]-(ch/2)), 2*a, ch, color='g', fill=True))
plt.show()
