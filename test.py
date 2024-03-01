from vpython import *

# Constants
G = 6.67430e-11  # Gravitational constant
m_sun = 1.989e30  # Mass of the sun in kg
m_earth = 5.972e24  # Mass of the Earth in kg
m_moon = 7.342e22  # Mass of the Moon in kg
r_earth = 149.6e9 / 1e8  # Average distance of Earth from Sun in 1e8 meters
r_moon = 384.4e6 / 1e8  # Average distance of Moon from Earth in 1e8 meters
v_earth = 29780 / 1e3  # Average velocity of Earth in km/s
v_moon = 1022 / 1e3  # Average velocity of Moon in km/s

# Define objects
sun = sphere(pos=vector(0,0,0), radius=0.696e8, color=color.yellow)
earth = sphere(pos=vector(r_earth,0,0), radius=6.371e6, color=color.blue, make_trail=True)
moon = sphere(pos=vector(r_earth + r_moon,0,0), radius=1.737e6, color=color.gray(0.5))

# Initial velocities
earth.velocity = vector(0, v_earth, 0)
moon.velocity = vector(0, v_earth + v_moon, 0)

# Time step
dt = 60  # in seconds

# Simulation loop
while True:
    rate(1000)
    
    # Calculate distance vectors
    r_earth_sun = sun.pos - earth.pos
    r_moon_earth = earth.pos - moon.pos
    r_moon_sun = sun.pos - moon.pos
    
    # Calculate gravitational forces
    F_earth_sun = G * m_sun * m_earth * r_earth_sun / mag(r_earth_sun)**3
    F_moon_earth = G * m_earth * m_moon * r_moon_earth / mag(r_moon_earth)**3
    F_moon_sun = G * m_sun * m_moon * r_moon_sun / mag(r_moon_sun)**3
    
    # Update velocities using F = ma
    earth.velocity += (F_earth_sun / m_earth) * dt + (F_moon_earth / m_earth) * dt
    moon.velocity += (F_moon_sun / m_moon) * dt + (F_moon_earth / m_moon) * dt
    
    # Update positions using v = dx/dt
    earth.pos += earth.velocity * dt
    moon.pos += moon.velocity * dt
