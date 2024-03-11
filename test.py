import matplotlib.pyplot as plt

import numpy as np

def plot_circle(center, radius, linestyle='solid', **kwargs):
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    plt.plot(x, y, linestyle=linestyle, **kwargs)

# Example usage
center = (0, 0)
radius = 1
plt.figure(figsize=(6, 6))
plot_circle(center, radius, linestyle='dashed', color='blue', linewidth=2)
plt.axis('equal')
plt.grid(True)
plt.show()