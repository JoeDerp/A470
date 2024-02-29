from vpython import *
import numpy as np

# Constants
G = 6.67e-11  # gravitational constant (m^3 kg^-1 s^-2)
dt = 0.01  # time step

# Create stationary sphere (planet)
sun = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.blue, make_trail=True)
sun.mass = 1500

# Create orbiting sphere (satellite)
orbiting_sphere = sphere(pos=vector(1, 0, 0), radius=0.2, color=color.red, make_trail=True)

# Initial conditions for satellite
orbiting_sphere.velocity = vector(0, 0, -100)  # initial velocity
orbiting_sphere.mass = 1000  # mass of the satellite

# # Create moon orbiting the satellite
# moon = sphere(pos=vector(1.3, 0, 0), radius=0.1, color=color.green, make_trail=True)

# # Initial conditions for moon
# moon.velocity = vector(0, 0, -50)  # initial velocity
# moon.mass = 1  # mass of the moon

# Define animation loop
while True:
    rate(100)  # Adjust the rate of animation as needed

    # Calculate the gravitational force between the satellite and the planet
    r = sun.pos - orbiting_sphere.pos
    force_satellite = G * sun.mass * orbiting_sphere.mass * r / mag(r) ** 3
    
    # Update satellite's velocity
    orbiting_sphere.velocity += force_satellite / orbiting_sphere.mass * dt
    
    # Update satellite's position
    orbiting_sphere.pos += orbiting_sphere.velocity * dt
    
    # # Calculate the gravitational force between the satellite and the moon
    # r = orbiting_sphere.pos - moon.pos
    # force_moon = G * orbiting_sphere.mass * moon.mass * r / mag(r) ** 3
    
    # # Update moon's velocity
    # moon.velocity += force_moon / moon.mass * dt
    
    # # Update moon's position
    # moon.pos += moon.velocity * dt
