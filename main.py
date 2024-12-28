import matplotlib.pyplot as plt;
import numpy as np;

#earth motion aroud the sun


# Constants
G = 6.67430e-11 # Gravitational constant
M = 1.989e30 # Mass of the sun

# Initial conditions
x0 = 147.09e9 # Initial x position
x1 = 0 # Initial y position
y0 = 0 # Initial x velocity
y1 = 30.29e3 # Initial y velocity

r_0 = np.array([x0, x1]) # Initial state vector
v_0 = np.array([y0, y1]) # Initial state vector

# Time step
dt = 3600 # Time step in seconds
t = 3.154e7 # Initial

# Simulation time
t_max = 365 * 24 * 60 * 60 # 1 year

# time array = np.arange(0, t_max, dt)

t_o = np.arange(0, t_max, dt)
print(t_o)
r =np.empty(shape=(len(t_o), 2))
v =np.empty(shape=(len(t_o), 2))

#set initial conditions
r[0], v[0] = r_0, v_0

