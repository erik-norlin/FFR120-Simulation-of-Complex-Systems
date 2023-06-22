# Exercise 2.2 (a) and (b).
import numpy as np
import matplotlib.pyplot as plt

# Initialize lattice
lattice_size = 200
lattice = np.sign(np.random.rand(lattice_size,lattice_size) - 0.5)
new_lattice = lattice.copy()
ten_percent = int(lattice_size*lattice_size/10)

# Constants
J = 1
H = 0
iterations = 100000

fig, axs = plt.subplots(3, 4, figsize=(12,12))
time_0 = lattice.copy()
temperatures = np.array([1, 2.269, 6])

# Performing MC over 3 different temperatures
for temp in range(len(temperatures)):

    T = temperatures[temp]
    beta = 1/T
    lattice = time_0.copy()

    # MC loop
    for time_step in range(iterations):

        # Update randomly 10% of the cells
        for update in range(ten_percent):

            i = np.random.randint(lattice_size) 
            j = np.random.randint(lattice_size)

            M = 0

            # Due to boundaries
            if i > 0:
                M += lattice[i-1,j]
            if i < lattice_size-1:
                M += lattice[i+1,j]
            if j > 0:
                M += lattice[i,j-1]
            if j < lattice_size-1:
                M += lattice[i,j+1]

            E_plus = -H-J*M
            E_minus = H+J*M

            prob_plus = np.exp(-beta*E_plus) / (np.exp(-beta*E_plus) + np.exp(-beta*E_minus))
            rnd = np.random.rand()

            if rnd < prob_plus:
                new_lattice[i,j] = 1
            else:
                new_lattice[i,j] = -1

        lattice = new_lattice.copy()

        # Snapshots of certain time steps
        if time_step == 100-1:
            time_1 = lattice.copy()
        elif time_step == 10000-1:
            time_2 = lattice.copy()
        elif time_step == 100000-1:
            time_3 = lattice.copy()

    # Plotting
    axs[temp,0].imshow(time_0)
    axs[temp,0].yaxis.set_ticks([])
    axs[temp,0].xaxis.set_ticks([])    

    axs[temp,1].imshow(time_1)
    axs[temp,1].yaxis.set_ticks([])
    axs[temp,1].xaxis.set_ticks([])

    axs[temp,2].imshow(time_2)
    axs[temp,2].yaxis.set_ticks([])
    axs[temp,2].xaxis.set_ticks([])

    axs[temp,3].imshow(time_3)
    axs[temp,3].yaxis.set_ticks([])
    axs[temp,3].xaxis.set_ticks([])

# Plotting
axs[0,0].set_ylabel('T = 1 < T_c')
axs[1,0].set_ylabel('T = 2.269 = T_c')
axs[2,0].set_ylabel('T = 6 > T_c')

axs[0,0].set_title('t = 0')
axs[0,1].set_title('t = 100')
axs[0,2].set_title('t = 10000')
axs[0,3].set_title('t = 100000')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('22ab.png', bbox_inches='tight')
plt.show()