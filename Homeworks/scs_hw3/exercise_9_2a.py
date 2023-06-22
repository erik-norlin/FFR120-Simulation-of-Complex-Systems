# Exercise 9.2a
import numpy as np
import matplotlib.pyplot as plt
import sys

T = 10000
ensembles = 100 
x = np.zeros((ensembles,T+1))
y = x.copy()
phi = 0
dt = 0.01
timesteps = int(T/dt)
t_iterations = np.linspace(0, T*dt, T+1)
# dt = tau*dt_step
# timesteps = int(tau/dt)*10s
# t = np.linspace(0, timesteps*dt_step, timesteps+1)

# Looping parameter
# Dt = 2*10**-12
# Dt = 5*10**-13 # OG
Dt = 8*10**-14

# Stretching parameter
# Dr = 0.05
# Dr = 0.5 # OG
Dr = 5

x_v0 = x.copy()
x_v1 = x.copy()
x_v2 = x.copy()
x_v3 = x.copy()

y_v0 = x.copy()
y_v1 = x.copy()
y_v2 = x.copy()
y_v3 = x.copy()

MSD_v0 = np.zeros((T+1))
MSD_v1 = MSD_v0.copy()
MSD_v2 = MSD_v0.copy()
MSD_v3 = MSD_v0.copy()

for ensemble in range(ensembles):
    
    v = 0
    for t in range(T):

        x_v0[ensemble,t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v0[ensemble,t]
        y_v0[ensemble,t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v0[ensemble,t]
        phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

    v = 1*10**-6
    for t in range(T):

        x_v1[ensemble,t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v1[ensemble,t]
        y_v1[ensemble,t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v1[ensemble,t]
        phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

    v = 2*10**-6
    for t in range(T):

        x_v2[ensemble,t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v2[ensemble,t]
        y_v2[ensemble,t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v2[ensemble,t]
        phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

    v = 3*10**-6
    for t in range(T):

        x_v3[ensemble,t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v3[ensemble,t]
        y_v3[ensemble,t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v3[ensemble,t]
        phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

for t in range(T):
    MSD_v0[t+1] = np.sum(x_v0[:,t+1]**2 + y_v0[:,t+1]**2) / ensembles
    MSD_v1[t+1] = np.sum(x_v1[:,t+1]**2 + y_v1[:,t+1]**2) / ensembles
    MSD_v2[t+1] = np.sum(x_v2[:,t+1]**2 + y_v2[:,t+1]**2) / ensembles
    MSD_v3[t+1] = np.sum(x_v3[:,t+1]**2 + y_v3[:,t+1]**2) / ensembles

fig, ax = plt.subplots()

xmax = 2*10**-5
ymax = xmax

ax.plot(t_iterations, MSD_v0, '-', linewidth=1.5, color='tab:blue', label='v=0')
ax.plot(t_iterations, MSD_v1, '-', linewidth=1.5, color='tab:green', label='v=1*1e-6')
ax.plot(t_iterations, MSD_v2, '-', linewidth=1.5, color='tab:orange', label='v=2*1e-6')
ax.plot(t_iterations, MSD_v3, '-', linewidth=1.5, color='tab:red', label='v=3*1e-6')
# ax.set_xlim([-xmax,xmax])
# ax.set_ylim([-ymax,ymax])
ax.set_box_aspect(1)
ax.set_ylabel('MSD (m^2)')
ax.set_xlabel('t (s)')
ax.set_yscale('log')
ax.set_xscale('log')

plt.legend(loc="upper left")
plt.savefig('exercise_9_2a_DtL_DrL_ENSEMBLE.png', bbox_inches='tight')
plt.show()