# Exercise 10.1b
import numpy as np
import matplotlib.pyplot as plt

T = 100
v0 = 5
vinf = 0.01

dt = 0.01
tau = 2
# dt = tau*dt_step
# timesteps = int(tau/dt)*10
# t = np.linspace(0, timesteps*dt_step, timesteps+1)
length = v0*tau/100

# 

# lambdas = np.linspace(0.1*length, 10*length, 20)
# c = 5

# r = np.zeros((len(lambdas), T))

# for lambd in range(len(lambdas)):

#     x = np.zeros((T+1))
#     y = x.copy()
#     phi = 0

#     for t in range(T):

#         r[lambd, t] = np.sqrt(x[t]**2 + y[t]**2)

#         I = (np.sin(2*np.pi*x[t]/lambd)) # 10.1b
#         # I = (np.sin(2*np.pi*(x[t]-c*(t+1))/lambdas[lambd])) # 10.1c
#         v = vinf+(v0-vinf)*np.exp(-I) 

#         x[t+1] = v*np.cos(phi)*dt + x[t]
#         y[t+1] = v*np.sin(phi)*dt + y[t]

#         phi = np.sqrt(2/tau)*np.random.normal() + phi


# r_average = np.zeros((len(lambdas)))
# for i in range(len(r[:,0])):
#     r_average[i] = np.sum(r[i,:])/len(r[0,:])

# fig, ax = plt.subplots()

# xmax = 5
# ymax = xmax

# ax.plot(lambdas, r_average)
# ax.set_xlabel('Lambda/length')
# ax.set_ylabel('<r> from origo')
# # ax.set_xlim([-xmax,xmax])
# # ax.set_ylim([-ymax,ymax])
# ax.set_box_aspect(1)
# plt.show()

no_lambdas = 3
# fig, axs = plt.subplots(1,no_lambdas, figsize=(10,10))
fig, ax = plt.subplots()

color = np.array(['red','orange','blue'])

lambdas = np.array([0.1*length, 1*length, 10*length])

# lambdas = np.linspace(0.1*length, 10*length, no_lambdas)
w = np.random.normal(0,1,size=(T))

for lambd in range(len(lambdas)):

    x = np.zeros((T+1))
    y = x.copy()
    phi = 0

    for t in range(T):

        I = (np.sin(2*np.pi*x[t]/lambdas[lambd]))**2 # 10.1b
        # I = (np.sin(2*np.pi*(x[t]-c*(t+1))/lambdas[lambd])) # 10.1c
        v = vinf+(v0-vinf)*np.exp(-I) 

        x[t+1] = v*np.cos(phi)*dt + x[t]
        y[t+1] = v*np.sin(phi)*dt + y[t]

        # phi = np.sqrt(2/tau)*np.random.normal() + phi
        phi = np.sqrt(2/tau)*w[t] + phi

    xmax = 1
    ymax = xmax
    # axs[lambd].plot(x, y)
    # axs[lambd].set_xlim([-xmax,xmax])
    # axs[lambd].set_ylim([-ymax,ymax])
    # axs[lambd].set_box_aspect(1)

    ax.plot(x, y, color[lambd],'-', linewidth=1)
    # ax.set_xlim([-xmax,xmax])
    # ax.set_ylim([-ymax,ymax])
    ax.set_box_aspect(1)

# axs[0].set_xlabel('x')
# axs[0].set_ylabel('<r> from origo')

plt.title('Lambda/length')
plt.show()