# Exercise 53b

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
time_step = 0.01
dt = tau*time_step

epochs = 10000
tau_trajectory = np.linspace(1,no_iterations,no_iterations)
x_weight_MSD = np.zeros(len(tau_trajectory))
x_weightless_MSD = np.zeros(len(tau_trajectory))
fig, ax = plt.subplots(figsize=(6,6))

for i_tau in range(len(tau_trajectory)):

    timesteps = int(tau/dt)*i_tau
    iterations = np.linspace(0, timesteps*time_step, timesteps+1)
    
    x = np.zeros((epochs,timesteps+1))
    x_weight = x.copy()
    x_weightless = x.copy()

    for epoch in range(epochs):
        
        for i in range(timesteps):
            w = np.random.normal()
            x_weight[epoch, i+1] = (x_weight[epoch, i] * (2 + (dt*gamma/m)) / (1 + (dt*gamma/m))) - (x_weight[epoch, i-1] / (1 + (dt*gamma/m))) + (dt**1.5 * w * np.sqrt(2*k*T*gamma) / (m + (dt*gamma)))
            x_weightless[epoch, i+1] = x_weightless[epoch, i] + (w * np.sqrt(2*k*T*dt/gamma))

    x_weight_MSD[i_tau] = np.sum(x_weight[:,-1]**2) / epochs
    x_weightless_MSD[i_tau] = np.sum(x_weightless[:,-1]**2) / epochs

    print(i_tau)

ax.plot(tau_trajectory, x_weight_MSD, '--', color='black', label='Inertia')
ax.plot(tau_trajectory, x_weightless_MSD, '-', color='tab:cyan', label='Non-inertia')
ax.set_xlabel('t/tau')
ax.set_ylabel('MSD (m^2)')
ax.set_box_aspect(1)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([2,100])
# 'linear', 'log', 'symlog', 'asinh', 'logit', 'function', 'functionlog'
plt.legend(loc="upper left")
plt.savefig('exercise_53bv2.png', bbox_inches='tight')
plt.show()