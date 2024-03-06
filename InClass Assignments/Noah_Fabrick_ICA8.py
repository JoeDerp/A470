from vpython import *
import numpy as np

sun = sphere(pos=vector(0,0,0),radius=0.8,color=color.yellow)
earth = sphere(pos=vector(5,0,0),radius=0.3,color=color.blue)
moon = sphere(pos=earth.pos+vector(1.5,0,0),radius=0.1,color=vector(0.5,0.5,0.5))

while True:
    rate(60)
    earth.rotate(angle=(2*np.pi)/365, axis=vector(0, 1, 0), origin=sun.pos)
    moon.rotate(angle=(2*np.pi)/24, axis=vector(0, 1, 0), origin=earth.pos)
