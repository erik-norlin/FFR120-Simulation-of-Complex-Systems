# Exercise 52b

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(10,10))
epochs = 10**4

delta_t_array = np.array([0.01, 0.05, 0.1])
color_array = np.array(['tab:blue', 'tab:green', 'tab:orange'])
time_trajectory = 10

for delta_t_i in range(len(delta_t_array)):

    delta_t = delta_t_array[delta_t_i]
    no_iterations = int(time_trajectory / delta_t)
    iterations = np.linspace(0, no_iterations, no_iterations+1)
    time_scale = no_iterations / time_trajectory

    x_t = np.zeros((epochs, no_iterations+1))
    x_t[:,0] = 0

    MSD = np.zeros((epochs, len(iterations)))
    MSD[:,0] = 0

    for epoch in range(epochs):
        for i in range(len(iterations)-1):
            rnd = np.random.normal()
            x_t[epoch,i+1] = x_t[epoch,i] + (rnd * np.sqrt(delta_t))
            MSD[epoch,i+1] = np.power(x_t[epoch,i+1], 2)

    MSD_average = np.zeros(len(MSD[0,:]))
    for i in range(len(MSD_average)):
        MSD_average[i] = np.sum(MSD[:,i]) / len(MSD[:,i])

    axs[delta_t_i].plot(iterations/time_scale, MSD_average, '.', markersize=2, color=color_array[delta_t_i] )
    axs[delta_t_i].set_xlabel('t (s)') 
    axs[delta_t_i].set_box_aspect(1)
    axs[delta_t_i].set_ylim([0,6])
    axs[delta_t_i].set_xlim([0,5])
    axs[delta_t_i].set_xticks((0, 1, 2, 3, 4, 5))
    axs[delta_t_i].set_yticks(())
    axs[delta_t_i].xaxis.set_tick_params(labelsize=7)
    axs[delta_t_i].yaxis.set_tick_params(labelsize=7)

axs[0].set_yticks((0, 1, 2, 3, 4, 5))
axs[0].set_ylabel('MSD') 
axs[0].set_title('delta_t = 0.01')
axs[1].set_title('delta_t = 0.05')
axs[2].set_title('delta_t = 0.1')

matplotlib.rc('xtick', labelsize=5) 
matplotlib.rc('ytick', labelsize=5) 

plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.savefig('exercise_52b.png', bbox_inches='tight')
plt.show()