# Exercise 10.1a
import numpy as np
import matplotlib.pyplot as plt

T = 1000
x = np.zeros((T+1))
y = x.copy()
phi = 0
v0 = 2
vinf = 0

dt = 0.01
tau = 2
# dt = tau*dt_step
# timesteps = int(tau/dt)*10
# t = np.linspace(0, timesteps*dt_step, timesteps+1)
length = v0*tau
lambd = length/10
c = 5

# plt.ion()

for t in range(T):
    
    # I = 0 # 10.1a
    # I = (np.sin(2*np.pi*x[t]/lambd)) # 10.1b
    I = (np.sin(2*np.pi*(x[t]-c*(t+1))/lambd)) # 10.1c
    v = vinf+(v0-vinf)*np.exp(-I) 

    x[t+1] = v*np.cos(phi)*dt + x[t]
    y[t+1] = v*np.sin(phi)*dt + y[t]

    phi = np.sqrt(2/tau)*np.random.normal() + phi

    # plt.axis([-50,50,-50,50])
    # plt.scatter(x[t],y[t])
    # plt.show()
    # plt.pause(0.005)
    # plt.clf()



fig, ax = plt.subplots()

xmax = 1
ymax = xmax

ax.plot(x, y, linewidth=1)
ax.set_xlim([-xmax,xmax])
ax.set_ylim([-ymax,ymax])
ax.set_box_aspect(1)
plt.show()