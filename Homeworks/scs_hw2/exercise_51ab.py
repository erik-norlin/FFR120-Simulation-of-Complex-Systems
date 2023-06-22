# Exercise 51ab

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 3, figsize=(10,10))
epochs = 1000
iterations = np.linspace(0,1000,1001)
x = np.zeros((epochs,1001))


# Coinflip
p_coinflip = 0.5
x_coinflip = x.copy()
x_coinflip[0] = 0

for epoch in range(epochs):
    for i in range(len(iterations)-1):
        rnd = np.sign(np.random.uniform() - 0.5)
        x_coinflip[epoch,i+1] = x_coinflip[epoch,i] + rnd

    axs[1,0].plot(x_coinflip[epoch,:], iterations, 'tab:blue', linewidth=0.3)

axs[0,0].bar([-1, 1], [0.5, 0.5], width=0.3, align='center', color='tab:blue')
axs[0,0].set_xlabel('delta x') 
axs[0,0].set_ylabel('p(delta x)') 
axs[0,0].set_box_aspect(1)
axs[0,0].set_xlim([-2,2])
axs[0,0].set_xticks((-2, -1, 0, 1, 2))
axs[0,0].set_yticks(())
axs[0,0].xaxis.set_tick_params(labelsize=7)
axs[0,0].yaxis.set_tick_params(labelsize=7)

axs[1,0].set_xlabel('x(t)') 
axs[1,0].set_ylabel('Time step, t') 
axs[1,0].set_box_aspect(1)
axs[1,0].set_xlim([-120,120])
axs[1,0].set_xticks((-100, -50, 0, 50, 100))
axs[1,0].set_yticks((0, 200, 400, 600, 800, 1000))
axs[1,0].xaxis.set_tick_params(labelsize=7)
axs[1,0].yaxis.set_tick_params(labelsize=7)

axs[2,0].hist(x_coinflip[:,-1], density=True, bins=50, color='tab:blue', alpha=0.5, histtype='bar', ec='black')
axs[2,0].set_xlabel('x_1000') 
axs[2,0].set_ylabel('p(x_1000)') 
axs[2,0].set_box_aspect(1)
axs[2,0].set_xlim([-120,120])
axs[2,0].set_xticks((-100, -50, 0, 50, 100))
# axs[2,0].set_yticks(())
axs[2,0].xaxis.set_tick_params(labelsize=7)
axs[2,0].yaxis.set_tick_params(labelsize=7)


# Gaussian
x_gaussian = x.copy()
x_gaussian[0] = 0

for epoch in range(epochs):
    for i in range(len(iterations)-1):
        rnd = np.sign(np.random.random() - 0.5)
        x_gaussian[epoch,i+1] = x_gaussian[epoch,i] + rnd

    axs[1,1].plot(x_gaussian[epoch,:], iterations, 'tab:green', linewidth=0.3)

N = 1000
x2 = [np.random.normal() for _ in range(N)]
axs[0,1].hist(x2, bins=50, color='tab:green', alpha=0.5, histtype='bar', ec='black')
axs[0,1].set_xlabel('delta x') 
axs[0,1].set_box_aspect(1)
axs[0,1].set_xlim([-5,5])
axs[0,1].set_xticks((-5, -2.5, 0, 2.5, 5))
axs[0,1].set_yticks(())
axs[0,1].xaxis.set_tick_params(labelsize=7)
axs[0,1].yaxis.set_tick_params(labelsize=7)

axs[1,1].set_xlabel('x(t)') 
axs[1,1].set_box_aspect(1)
axs[1,1].set_xlim([-120,120])
axs[1,1].set_xticks((-100, -50, 0, 50, 100))
axs[1,1].set_yticks(())
axs[1,1].xaxis.set_tick_params(labelsize=7)
axs[1,1].yaxis.set_tick_params(labelsize=7)

axs[2,1].hist(x_gaussian[:,-1], density=True, bins=50, color='tab:green', alpha=0.5, histtype='bar', ec='black')
axs[2,1].set_xlabel('x_1000') 
axs[2,1].set_box_aspect(1)
axs[2,1].set_xlim([-120,120])
axs[2,1].set_xticks((-100, -50, 0, 50, 100))
# axs[2,1].set_yticks(())
axs[2,1].xaxis.set_tick_params(labelsize=7)
axs[2,1].yaxis.set_tick_params(labelsize=7)


# Step
x_step = x.copy()
x_step[0] = 0

for epoch in range(epochs):
    for i in range(len(iterations)-1):
        rnd = np.random.random()
        if rnd < 1/3:
            x_step[epoch,i+1] = x_step[epoch,i] + (-1)
        elif rnd < 2/3:
            x_step[epoch,i+1] = x_step[epoch,i] + (1 - np.sqrt(3))/2
        elif rnd < 3/3:
            x_step[epoch,i+1] = x_step[epoch,i] + (1 + np.sqrt(3))/2
            
    axs[1,2].plot(x_step[epoch,:], iterations, 'tab:orange', linewidth=0.3)

a = (1 - np.sqrt(3))/2
b = (1 + np.sqrt(3))/2
axs[0,2].bar([-1, a, b], [1/3, 1/3, 1/3], width=0.3, align='center', color='tab:orange')
axs[0,2].set_xlabel('delta x') 
axs[0,2].set_box_aspect(1)
axs[0,2].set_xlim([-2,2])
axs[0,2].set_xticks((-1, a, b))
axs[0,2].set_yticks(())
axs[0,2].xaxis.set_tick_params(labelsize=7)
axs[0,2].yaxis.set_tick_params(labelsize=7)

axs[1,2].set_xlabel('x(t)') 
axs[1,2].set_box_aspect(1)
axs[1,2].set_xlim([-120,120])
axs[1,2].set_xticks((-100, -50, 0, 50, 100))
axs[1,2].set_yticks(())
axs[1,2].xaxis.set_tick_params(labelsize=7)
axs[1,2].yaxis.set_tick_params(labelsize=7)

axs[2,2].hist(x_step[:,-1], density=True, bins=50, color='tab:orange', alpha=0.5, histtype='bar', ec='black')
axs[2,2].set_xlabel('x_1000') 
axs[2,2].set_box_aspect(1)
axs[2,2].set_xlim([-120,120])
axs[2,2].set_xticks((-100, -50, 0, 50, 100))
# axs[2,2].set_yticks(())
axs[2,2].xaxis.set_tick_params(labelsize=7)
axs[2,2].yaxis.set_tick_params(labelsize=7)


axs[0,0].set_title('Coin flip')
axs[0,1].set_title('Gaussian')
axs[0,2].set_title('Asymmetric step')

matplotlib.rc('xtick', labelsize=5) 
matplotlib.rc('ytick', labelsize=5) 

plt.subplots_adjust(wspace=0.01, hspace=0.5)
plt.savefig('exercise_51ab.png', bbox_inches='tight')
plt.show()