import numpy as np
import matplotlib.pyplot as plt

def ackley(xx, a=20, b=0.2, c=2*np.pi):
    d = len(xx)
    sum1 = 0
    sum2 = 0
    for ii in range(d):
        xi = xx[ii]
        sum1 += xi**2
        sum2 += np.cos(c * xi)
    
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    
    y = term1 + term2 + a + np.exp(1)
    
    return y

# Example usage:
xi = np.linspace(-32.768,32.768,100)
xx = [xi,xi]  # Example input vector xx
result = ackley(xx)

# x, y = np.meshgrid(xi, xi)

# Number of points along each dimension
num_points = 100

# Generate coordinates along each dimension
x_values = xi
y_values = xi
z_values = xi

# Create a meshgrid for 3D points
x_mesh, y_mesh, z_mesh = np.meshgrid(x_values, y_values, z_values)

# Flatten the meshgrid to get a list of 3D points
points_3d = np.column_stack((x_mesh.flatten(), y_mesh.flatten(), z_mesh.flatten()))

# plt.contourf(x, y, result, cmap='viridis')
# plt.colorbar(label='Function value')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Ackley Function')

# plt.show()

print(x_mesh)
print(x_mesh.flatten())