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

t_0 = np.arange(0, t_max, dt)
print(t_0)
r =np.empty(shape=(len(t_0), 2))
v =np.empty(shape=(len(t_0), 2))

#set initial conditions
r[0], v[0] = r_0, v_0

def acc(r):
  return ((-G * M / np.linalg.norm(r)**3) * r)

# def eulerMethod(r, v, acc, dt):
#     for i in range(1, len(t_0)):
#         r[i] =r[i-1] + v[i-1] * dt
#         v[i] =v[i-1] +acc(r[i-1]) * dt

# eulerMethod(r, v, acc, dt)

# print(f"Max position: {max_position/1e7}, velocity at aphilion: {vel_aphilion/1e3}") 

def rk4_method(r, v, acc, dt):
    for i in range(1, len(r)):
        # Step 1
        k1v = acc(r[i-1])
        k1r = v[i-1]

        # Step 2
        k2v = acc(r[i-1] + 0.5 * dt * k1r)
        k2r = v[i-1] + 0.5 * dt * k1v

        # Step 3
        k3v = acc(r[i-1] + 0.5 * dt * k2r)
        k3r = v[i-1] + 0.5 * dt * k2v

        # Step 4
        k4v = acc(r[i-1] + dt * k3r)
        k4r = v[i-1] + dt * k3v

        r[i] = r[i-1] + (dt / 6.0) * (k1r + 2 * k2r + 2 * k3r + k4r)
        v[i] = v[i-1] + (dt / 6.0) * (k1v + 2 * k2v + 2 * k3v + k4v)

rk4_method(r, v, acc, dt)

sizes =np.array([np.linalg.norm(postion) for postion in r])
max_position = np.max(sizes)
arg_aphilion = np.argmax(sizes)
vel_aphilion = np.linalg.norm(v[arg_aphilion]) 

print(f"Max position: {max_position/1e9}, velocity at aphilion: {vel_aphilion/1e3}") 


