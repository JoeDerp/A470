import GooseModule.py as gse
import numpy as np
import matplotlib.pyplot as plt

# Intialization
numGeese = 20
geese = []
for g in range(numGeese):
    xRand = np.random.uniform(0,numGeese*2,2)
    plt.plot(xRand[0],xRand[1],'b^')
    plt.xlim(0,2*numGeese)
    plt.ylim(0,2*numGeese)
    geese.append(gse.Goose(xRand))

plt.show()
