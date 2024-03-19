# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y1 = [10, 15, 20, 18, 25]
# y2 = [3, 5, 8, 6, 10]

# fig, ax1 = plt.subplots()

# # Plot data for the first y-axis
# ax1.plot(x, y1, 'b*')
# ax1.set_xlabel('X axis')
# ax1.set_ylabel('Y axis 1', color='b')

# # Create a second y-axis sharing the same x-axis
# ax2 = ax1.twinx()
# ax2.plot(x, y2, 'r*')
# ax2.set_ylabel('Y axis 2', color='r')

# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
num_plots = 3  # Number of plots

# Create multiple figures using a loop
for i in range(num_plots):
    fig, ax = plt.subplots()  # Create a new figure and axis for each plot
    y = np.sin(x + i)  # Example function, you can replace it with your data
    ax.plot(x, y)
    ax.set_title(f'Plot {i+1}')  # Set title for each plot
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax2 = ax.twinx()
    ax2.plot(x, [yi+3 for yi in y], 'r*')
    ax2.set_ylabel('Y axis 2', color='r')

plt.show()
