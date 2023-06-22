# Exercise 9.2b
import numpy as np
import matplotlib.pyplot as plt
import sys

T = 10000
x = np.zeros((T+1))
y = x.copy()
phi = 0
dt = 0.01
timesteps = int(T/dt)
# dt = tau*dt_step
# timesteps = int(tau/dt)*10s
# t = np.linspace(0, timesteps*dt_step, timesteps+1)

# Looping parameter
Dt = 2*10**-12
# Dt = 5*10**-13 # OG
# Dt = 8*10**-14

# Stretching parameter
Dr = 0.05
# Dr = 0.5 # OG
# Dr = 5

x_v0 = x.copy()
x_v1 = x.copy()
x_v2 = x.copy()
x_v3 = x.copy()

y_v0 = x.copy()
y_v1 = x.copy()
y_v2 = x.copy()
y_v3 = x.copy()

# Simulation
v = 0
for t in range(T):

    x_v0[t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v0[t]
    y_v0[t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v0[t]
    phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

v = 1*10**-6
for t in range(T):

    x_v1[t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v1[t]
    y_v1[t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v1[t]
    phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

v = 2*10**-6
for t in range(T):

    x_v2[t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v2[t]
    y_v2[t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v2[t]
    phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

v = 3*10**-6
for t in range(T):

    x_v3[t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x_v3[t]
    y_v3[t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y_v3[t]
    phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

# Time averged MSD
t_range = int(T/2 + 1)
t_iterations = np.linspace(0, T*dt, t_range)

MSD_v0_time = np.zeros((t_range,t_range))
MSD_v1_time = MSD_v0_time.copy()
MSD_v2_time = MSD_v0_time.copy()
MSD_v3_time = MSD_v0_time.copy()

MSD_v0 = np.zeros((t_range))
MSD_v1 = MSD_v0.copy()
MSD_v2 = MSD_v0.copy()
MSD_v3 = MSD_v0.copy()

for i in range(len(x_v0)-t_range+1):

    x_row_v0 = x_v0[i:i+t_range]
    y_row_v0 = y_v0[i:i+t_range]
    for j in range(len(y_row_v0)):
        MSD_v0_time[i,j] = (x_row_v0[j] - x_row_v0[0])**2 + (y_row_v0[j] - y_row_v0[0])**2

    x_row_v1 = x_v1[i:i+t_range]
    y_row_v1 = y_v1[i:i+t_range]
    for j in range(len(y_row_v1)):
        MSD_v1_time[i,j] = (x_row_v1[j] - x_row_v1[0])**2 + (y_row_v1[j] - y_row_v1[0])**2

    x_row_v2 = x_v2[i:i+t_range]
    y_row_v2 = y_v2[i:i+t_range]
    for j in range(len(y_row_v2)):
        MSD_v2_time[i,j] = (x_row_v2[j] - x_row_v2[0])**2 + (y_row_v2[j] - y_row_v2[0])**2
    
    x_row_v3 = x_v3[i:i+t_range]
    y_row_v3 = y_v3[i:i+t_range]
    for j in range(len(y_row_v3)):
        MSD_v3_time[i,j] = (x_row_v3[j] - x_row_v3[0])**2 + (y_row_v3[j] - y_row_v3[0])**2

for i in range(t_range):
    MSD_v0[i] = np.sum(MSD_v0_time[:,i])
    MSD_v1[i] = np.sum(MSD_v1_time[:,i])
    MSD_v2[i] = np.sum(MSD_v2_time[:,i])
    MSD_v3[i] = np.sum(MSD_v3_time[:,i])

MSD_v0 = MSD_v0 / t_range
MSD_v1 = MSD_v1 / t_range
MSD_v2 = MSD_v2 / t_range
MSD_v3 = MSD_v3 / t_range

# t = 0
# for i in range(t_range):
#     for j in range(t_range):

#         MSD_v0[i] += (x_v0[t+j] - x_v0[t])**2 + (y_v0[t+j] - y_v0[t])**2 
#         t += 1

# MSD_v0 = MSD_v0 / t_range

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
plt.savefig('exercise_9_2b_DtS_DrS_TIME.png', bbox_inches='tight')
plt.show()