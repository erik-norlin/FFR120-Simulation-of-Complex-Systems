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
time_step = 0.01
dt = tau*time_step
tau_trajectory = 10000
timesteps = int(tau/dt)*tau_trajectory
iterations = np.linspace(0, timesteps*time_step, timesteps+1)
epochs = 100

# Ensemble average MSD
x = np.zeros((epochs,timesteps+1))
# x_weight = x.copy()
x_weightless = x.copy()
x_weight_ensemble_MSD = np.zeros(timesteps+1)
x_weightless_ensemble_MSD = np.zeros(timesteps+1)

for epoch in range(epochs):
    
    for i in range(timesteps):
        w = np.random.normal()
        # x_weight[epoch,i+1] = (x_weight[epoch,i] * (2 + (dt*gamma/m)) / (1 + (dt*gamma/m))) - (x_weight[epoch,i-1] / (1 + (dt*gamma/m))) + (dt**1.5 * w * np.sqrt(2*k*T*gamma) / (m + (dt*gamma)))
        x_weightless[epoch,i+1] = x_weightless[epoch,i] + (w * np.sqrt(2*k*T*dt/gamma))
    
    print(epoch)

for i in range(timesteps):
    # x_weight_ensemble_MSD[i+1] = np.sum(x_weight[:,i]**2) / epochs
    x_weightless_ensemble_MSD[i+1] = np.sum(x_weightless[:,i]**2) / epochs

fig, axs = plt.subplots(1,2,figsize=(10,10))

# axs[0].plot(iterations, x_weight_ensemble_MSD, '--', color='black')
axs[0].plot(iterations, x_weightless_ensemble_MSD, '-', color='tab:cyan')
axs[0].set_xlabel('t/tau')
axs[0].set_ylabel('MSD (m^2)')
axs[0].set_title('Ensemble averaged MSD')
axs[0].set_box_aspect(1)

# Time average MSD
x = np.zeros((timesteps+1))
x_weight = x.copy()
x_weightless = x.copy()
x_weight_time_MSD = np.zeros(timesteps+1)
x_weightless_time_MSD = np.zeros(timesteps+1)

for i in range(timesteps):
    w = np.random.normal()
    # x_weight[i+1] = (x_weight[i] * (2 + (dt*gamma/m)) / (1 + (dt*gamma/m))) - (x_weight[i-1] / (1 + (dt*gamma/m))) + (dt**1.5 * w * np.sqrt(2*k*T*gamma) / (m + (dt*gamma)))
    x_weightless[i+1] = x_weightless[i] + (w * np.sqrt(2*k*T*dt/gamma))

    # x_weight_time_MSD[i+1] = x_weight[i]**2 / timesteps
    x_weightless_time_MSD[i+1]= x_weightless[i]**2 / timesteps

    if i % 1000 == 0:
        print(i)

# axs[1].plot(iterations, x_weight_time_MSD, '--', color='black', label='Inertia')
axs[1].plot(iterations, x_weightless_time_MSD, '-', color='tab:cyan', label='Non-inertia')
axs[1].set_xlabel('t/tau')
axs[1].set_box_aspect(1)
axs[1].set_title('Time averaged MSD')

# plt.legend(loc="upper left")
plt.savefig('exercise_53c.png', bbox_inches='tight')
plt.show()