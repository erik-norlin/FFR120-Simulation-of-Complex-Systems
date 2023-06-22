# Exercise 54c

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
time_step = 0.001
dt = tau*time_step
tau_trajectory = 10
timesteps = int(tau/dt)*tau_trajectory
iterations = np.linspace(0, timesteps*time_step, timesteps+1)
x = np.zeros(timesteps+1) 
y = np.zeros(timesteps+1) 
epochs = 10
cx = np.zeros((epochs,timesteps+1))
cy = np.zeros((epochs,timesteps+1))
cx_average = np.zeros(timesteps+1)
cy_average = np.zeros(timesteps+1)

for epoch in range(epochs):
    for i in range(timesteps-1):
        w = np.random.normal()
        x[i+1] = x[i] - (dt*x[i]*kx/gamma) + (w*np.sqrt(2*k*T*dt/gamma))
        w = np.random.normal()
        y[i+1] = y[i] - (dt*y[i]*ky/gamma) + (w*np.sqrt(2*k*T*dt/gamma))

    print(timesteps)
    for i in range(timesteps):
        if i % 100 == 0:
            print(i)
        for j in range(timesteps-i):
            cx[epoch,j] = cx[epoch,j] + x[i]*x[i+j]
            cy[epoch,j] = cy[epoch,j] + y[i]*y[i+j]
        cx[epoch,i] = cx[epoch,i]/(timesteps-i)
        cy[epoch,i] = cy[epoch,i]/(timesteps-i)
    cx[epoch,:] = cx[epoch,:]/timesteps
    cy[epoch,:] = cy[epoch,:]/timesteps

    print(epoch)

for i in range(timesteps):
    cx_average[i] = np.sum(cx[:,i]) / epochs
    cy_average[i] = np.sum(cy[:,i]) / epochs

t = np.linspace(0, 17*tau, timesteps+1)
cx_theory = (k*T/kx)*np.exp(-(kx*t/gamma))
cy_theory = (k*T/ky)*np.exp(-(ky*t/gamma))

fig, ax = plt.subplots(1,2,figsize=(10,10))

ax[0].plot(t, cx_average, '-', color='tab:blue', label='Autocorrelation')
ax[0].plot(t, cx_theory, '--', color='red', label='Theory')
ax[0].set_xlabel('t (s)')
ax[0].set_ylabel('C_x')
ymax = 2/10**14
ymin = -1/10**15
ax[0].set_ylim([ymin,ymax])
ax[0].legend(loc="upper right",prop={'size': 8})
ax[0].set_box_aspect(1)
ax[0].set_yticks(())

ax[1].plot(t, cy_average, '-', color='tab:green', label='Autocorrelation')
ax[1].plot(t, cy_theory, '--', color='red', label='Theory')
ax[1].set_xlabel('t (s)')
ax[1].set_ylabel('C_y')
ax[1].set_yticks(())
ax[1].set_ylim([ymin,ymax])
ax[1].legend(loc="upper right",prop={'size': 8})
ax[1].set_box_aspect(1)

plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.savefig('exercise_54c.png', bbox_inches='tight')
plt.show()
