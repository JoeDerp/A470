import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create some data
t = np.linspace(0, 2*np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set limits for the axes
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, 2*np.pi)

# Create a point
point, = ax.plot([], [], [], 'ro')  # 'ro' means red circle marker

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    point.set_3d_properties([])
    return point,

# Animation function: this is called sequentially
def animate(i):
    point.set_data(x[i], y[i])  # Update the position of the point in 2D
    point.set_3d_properties(z[i])  # Update the position of the point in 3D
    return point,

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True)

# Show the plot
plt.show()
