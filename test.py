import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Define the coordinates of the arrow's start and end points
x_start, y_start = 0.1, 0.2
x_end, y_end = 0.7, 0.7

# Draw the arrow
ax.arrow(x_start, y_start, x_end - x_start, y_end - y_start)

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Show the plot
plt.show()
