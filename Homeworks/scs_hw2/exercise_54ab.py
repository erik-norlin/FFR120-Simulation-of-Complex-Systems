# Exercise 54ab

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import sys

n = 0.001
R = 1/10**6
gamma = 6*np.pi*n*R
k = 1.380649/10**23
T = 300
kx = (1/10**12) / (1/10**6)
ky = (0.25/10**12) / (1/10**6)
tau = gamma / kx # Arbitary choose kx 
time_step = 0.01
dt = tau*time_step
tau_trajectory = 10000
timesteps = int(tau/dt)*tau_trajectory
iterations = np.linspace(0, timesteps*time_step, timesteps+1)
x = np.zeros(timesteps+1) 
y = np.zeros(timesteps+1) 

for i in range(timesteps-1):
    w = np.random.normal()
    x[i+1] = x[i] - (dt*x[i]*kx/gamma) + (w*np.sqrt(2*k*T*dt/gamma))
    w = np.random.normal()
    y[i+1] = y[i] - (dt*y[i]*ky/gamma) + (w*np.sqrt(2*k*T*dt/gamma))

xmax = 5/10**7
ymax = 7*10**6
x_sym = np.linspace(-xmax, xmax, timesteps)
y_sym = x_sym
px = 6*10**6*np.exp(-(0.5*kx*x_sym**2)/(k*T))
py = 3*10**6*np.exp(-(0.5*ky*y_sym**2)/(k*T))

fig, axs = plt.subplots(1,3,figsize=(12,12))

axs[0].plot(x, y, '.', color='tab:blue', markersize=0.1)
axs[0].set_xlabel('x (m)')
axs[0].set_ylabel('y (m)')
axs[0].set_xlim([-xmax, xmax])
axs[0].set_ylim([-xmax, xmax])
axs[0].set_box_aspect(1)

weights_x = 30*np.ones_like(x)/len(x)
weights_y = 30*np.ones_like(y)/len(y)

axs[1].hist(x, density=True, bins=100, color='tab:blue', alpha=0.5, label='Brownian')
axs[1].plot(x_sym, px, '--', color='red', label='Theory')
axs[1].set_xlabel('x (m)')
axs[1].set_ylabel('p(x)')
axs[1].set_box_aspect(1) 
axs[1].set_xlim([-xmax, xmax])
axs[1].legend(loc="upper left",prop={'size': 8})
axs[1].set_ylim([0, ymax])
axs[1].set_yticks(())

axs[2].hist(y, density=True, bins=100, color='tab:green', alpha=0.5, label='Brownian')
axs[2].plot(y_sym, py, '--', color='red', label='Theory')
axs[2].set_xlabel('y (m)')
axs[2].set_ylabel('p(y)')
axs[2].set_box_aspect(1)
axs[2].set_xlim([-xmax, xmax])
axs[2].legend(loc="upper left",prop={'size': 8})
axs[2].set_ylim([0, ymax])
axs[2].set_yticks(())

plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.savefig('exercise_54ab.png', bbox_inches='tight')
plt.show()
