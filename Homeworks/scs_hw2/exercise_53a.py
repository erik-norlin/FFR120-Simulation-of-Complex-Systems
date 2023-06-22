# Exercise 53a

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import sys

n = 0.001
R = 1/10**6
pi = np.pi
gamma = 6*pi*R*n
T = 300
k = 1.380649/10**23
m = 1.11/10**14
tau = m/gamma
no_iterations = 100
dt = tau*0.01

# 1 tau long trajectory
timesteps = int(tau/dt)
iterations = np.linspace(0, 1, timesteps+1)
x = np.zeros(timesteps+1)
x_weight = x.copy()
x_weightless = x.copy()

for i in range(timesteps):
    w = np.random.normal()
    x_weight[i+1] = (x_weight[i] * (2 + (dt*gamma/m)) / (1 + (dt*gamma/m))) - (x_weight[i-1] / (1 + (dt*gamma/m))) + (dt**1.5 * w * np.sqrt(2*k*T*gamma) / (m + (dt*gamma)))
    x_weightless[i+1] = x_weightless[i] + (w * np.sqrt(2*k*T*dt/gamma))

fig, axs = plt.subplots(1,2, figsize=(10,10))

axs[0].plot(iterations, x_weight, '--', color='black', label='Inertia')
axs[0].plot(iterations, x_weightless, color='tab:cyan', label='Non-inertia')
axs[0].set_xlabel('t/tau')
axs[0].set_ylabel('x (m)')
axs[0].set_box_aspect(1)


# 100 tau long trajectory
timesteps = int(tau/dt)*100
iterations = np.linspace(0, 100, timesteps+1)
x = np.zeros(timesteps+1)
x_weight = x.copy()
x_weightless = x.copy()

for i in range(timesteps):
    w = np.random.normal()
    x_weight[i+1] = (x_weight[i] * (2 + (dt*gamma/m)) / (1 + (dt*gamma/m))) - (x_weight[i-1] / (1 + (dt*gamma/m))) + (dt**1.5 * w * np.sqrt(2*k*T*gamma) / (m + (dt*gamma)))
    x_weightless[i+1] = x_weightless[i] + (w * np.sqrt(2*k*T*dt/gamma))

axs[1].plot(iterations, x_weight, '--', color='black', label='Inertia')
axs[1].plot(iterations, x_weightless, color='tab:cyan', linewidth=0.7, label='Non-inertia')
axs[1].set_xlabel('t/tau')
axs[1].set_box_aspect(1)

plt.legend(loc="upper left")
plt.savefig('exercise_53a.png', bbox_inches='tight')
plt.show()