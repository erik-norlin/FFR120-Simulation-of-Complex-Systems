# Exercise 9.3a,b,c,d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import sys

T = 1000
dt = 0.000001
timesteps = int(T/dt)
t_iterations = np.linspace(0, T*dt, T+1)
Dt = 0.1*10**-6
# Dt = 0.1*10**-8
Dr = 1
# Dr = 0.01
v = 3*10**-6
R = 1*10**-6

N = 100 # No. particles 
x = (np.random.rand(N,T+1)-0.5)*4*10**-5
y = (np.random.rand(N,T+1)-0.5)*4*10**-5
# d = np.zeros((N))
phi = (np.random.rand(N)-0.5)*2*np.pi

xmax = 2.5*10**-5
ymax = xmax
boundary_condition = xmax + R
marker_size = 20
fps_ani = 200
interval_ani = 0.01

fig, ax = plt.subplots(figsize=(7,7))

for t in range(T):

    # Computing new positions
    for n in range(N):

        x[n,t+1] = (v*np.cos(phi[n])*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x[n,t]
        y[n,t+1] = (v*np.sin(phi[n])*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y[n,t]
        phi[n] = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi[n]

    # Applying volume extraciton
    for n in range(N):

        distances = ((x[:,t+1]-x[n,t+1])**2 + (y[:,t+1]-y[n,t+1])**2)**0.5  
        angles = np.arctan2(y[:,t+1]-y[n,t+1], x[:,t+1]-x[n,t+1])
        overlapp = distances < (2*R)
        overlapp[n] = False

        for i in np.where(overlapp)[0]:
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
        # ax.plot(x_point, y_point, color='tab:blue', marker='.', markersize=marker_size)
        ax.add_patch(plt.Circle([x_point, y_point], radius=R, color='tab:blue'))
    ax.set_xlim([-xmax, xmax])
    ax.set_ylim([-ymax, ymax])

ax.set_ylabel('y (m)')
ax.set_xlabel('x (m)')
ax.set_box_aspect(1)
ani = FuncAnimation(fig, animate, frames=len(x[0,:]), interval=interval_ani)
ani.save('exercise_9_3c_VE_dt0.000001_T1000_Dt0.1e-6_Dr1.gif', writer=PillowWriter(fps=fps_ani))
plt.show()