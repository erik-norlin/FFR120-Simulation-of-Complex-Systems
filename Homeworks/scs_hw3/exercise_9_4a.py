# Exercise 9.4, 9.5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import sys

T = 100
dt = 0.3
timesteps = int(T/dt)
t_iterations = np.linspace(0, T*dt, T+1)
R = 1*10**-6
gamma = 6*np.pi*0.001*R
kB = 1.380649*10**-23
Dt = kB*300/gamma
# print(Dt)
# sys.exit()
Dt2 = kB*300/(8*np.pi*0.001*R**3)
# Dt = 0.1*10**-6
# Dt = 0.1*10**-8
Dr = 1
# Dr = 0.01
v = 3*10**-6

N = 50 # No. particles 
x = (np.random.rand(N,T+1)-0.5)*8*10**-5
y = (np.random.rand(N,T+1)-0.5)*8*10**-5
phi = (np.random.rand(N)-0.5)*2*np.pi

vpx = np.zeros(N)
vpy = np.zeros(N)
v0 = 50*10**-6

xmax = 50*10**-6
ymax = xmax
boundary_condition = xmax + R
marker_size = 20
fps_ani = 200
interval_ani = 0.01

fig, ax = plt.subplots(figsize=(7,7))

for t in range(T):

    # Computing new positions
    for n in range(N):

        x[n,t+1] = v*np.cos(phi[n])*dt + ((2*Dt*dt)**0.5)*np.random.normal(0,1) + vpx[n]*dt + x[n,t]
        y[n,t+1] = v*np.sin(phi[n])*dt + ((2*Dt*dt)**0.5)*np.random.normal(0,1) + vpy[n]*dt + y[n,t]
        phi[n] = ((2*Dr*Dt2*dt)**0.5)*np.random.normal(0,1) + phi[n]
        # phi[n] = ((2*Dr*dt)**0.5)*np.random.normal(0,1) + phi[n]

    vpx = np.zeros(N)
    vpy = np.zeros(N) 

    for n in range(N):

        distances = ((x[:,t+1]-x[n,t+1])**2 + (y[:,t+1]-y[n,t+1])**2)**0.5
        angles = np.arctan2(y[:,t+1]-y[n,t+1], x[:,t+1]-x[n,t+1])

        interact = distances < 5*R
        interact[n] = False

        for i in np.where(interact)[0]:
            vpx[n] = vpx[n] + (v0*R**2 / distances[i]**2) * np.cos(angles[i]) * distances[i]
            vpy[n] = vpy[n] + (v0*R**2 / distances[i]**2) * np.sin(angles[i]) * distances[i]

    # Applying volume extraciton
    # for i in range(3):
    for n in range(N):

        distances = ((x[:,t+1]-x[-n,t+1])**2 + (y[:,t+1]-y[n,t+1])**2)**0.5  
        angles = np.arctan2(y[:,t+1]-y[n,t+1], x[:,t+1]-x[n,t+1])
        overlap = distances < (2*R)
        overlap[n] = False

        for i in np.where(overlap)[0]:
            x[n,t+1] = x[n,t+1] + (distances[i] - 2*R)*np.cos(angles[i])/2
            y[n,t+1] = y[n,t+1] + (distances[i] - 2*R)*np.sin(angles[i])/2
            x[i,t+1] = x[i,t+1] - (distances[i] - 2*R)*np.cos(angles[i])/2
            y[i,t+1] = y[i,t+1] - (distances[i] - 2*R)*np.sin(angles[i])/2

        # Boundary condition
        if x[n,t+1] > boundary_condition:
            x[n,t+1] = -boundary_condition 

        elif x[n,t+1] < -boundary_condition:
            x[n,t+1] = boundary_condition

        if y[n,t+1] > boundary_condition:
            y[n,t+1] = -boundary_condition

        elif y[n,t+1] < -boundary_condition:
            y[n,t+1] = boundary_condition

def animate(i):
    ax.clear()
    for n in range(N):
        x_point = x[n,i]
        y_point = y[n,i]
        ax.add_patch(plt.Circle([x_point, y_point], radius=R, color='tab:blue'))
    ax.set_xlim([-xmax, xmax])
    ax.set_ylim([-ymax, ymax])

ax.set_ylabel('y (m)')
ax.set_xlabel('x (m)')
ax.set_box_aspect(1)
ani = FuncAnimation(fig, animate, frames=len(x[0,:]), interval=interval_ani)
ani.save('exercise_9_5_v0_50_test.gif', writer=PillowWriter(fps=fps_ani))
plt.show()