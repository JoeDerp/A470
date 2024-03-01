from vpython import *
import numpy as np

sun = sphere(pos=vector(0,0,0),radius=0.4,color=color.yellow)
earth = sphere(pos=vector(5,0,0),radius=0.1,color=color.blue)

while True:
    rate(60)
    earth.rotate(angle=1, axis=vector(0, 1, 0), origin=sun.pos)
