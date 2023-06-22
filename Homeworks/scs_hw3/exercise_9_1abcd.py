# Exercise 9.1abcd
import numpy as np
import matplotlib.pyplot as plt

T = 500
x = np.zeros((T+1))
y = x.copy()
phi = 0
dt = 0.01
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

# Total length parameter
# v = 0
# v = 1*10**-6
# v = 2*10**-6
v = 3*10**-6 # OG

for t in range(T):

    x[t+1] = (v*np.cos(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + x[t]
    y[t+1] = (v*np.sin(phi)*dt + ((2*Dt)**0.5)*np.random.normal(0,1)*(dt**0.5)) + y[t]
    phi = ((2*Dr)**0.5)*np.random.normal(0,1)*(dt**0.5) + phi

fig, ax = plt.subplots()

xmax = 2*10**-5
ymax = xmax

ax.plot(x, y, '-', linewidth=3, color='tab:red')
ax.set_xlim([-xmax,xmax])
ax.set_ylim([-ymax,ymax])
ax.set_box_aspect(1)
ax.set_ylabel('y (m)')
ax.set_xlabel('x (m)')

plt.savefig('exercise_9_1ab_v3_DrL.png', bbox_inches='tight')
plt.show()