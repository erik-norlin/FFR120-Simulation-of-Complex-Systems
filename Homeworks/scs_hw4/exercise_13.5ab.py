# Exercise 13.5ab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def play_game(self_strat, neighbor_strat):

    coop = True
    defect = False
    self_previous = coop
    neighbor_previous = coop
    self_punishment = 0

    for round in range(1,N+1):

        if round <= self_strat and neighbor_previous == coop:
            self_action = coop
        else:
            self_action = defect

        if round <= neighbor_strat and self_previous == coop:
            neighbor_action = coop
        else:
            neighbor_action = defect

        if self_action == coop and neighbor_action == coop:
            self_punishment += R
        elif self_action == coop and neighbor_action == defect:
            self_punishment += S
        elif self_action == defect and neighbor_action == coop:
            self_punishment += T
        elif self_action == defect and neighbor_action == defect:
            self_punishment += P

        self_previous = self_action
        neighbor_previous = neighbor_action

    return self_punishment

N = 7
T = 0
R = 0.46
P = 1
S = 1.5
mu = 0.01
timesteps = 500

L = 30
strat_array = np.random.randint(0,N+1,size=(L,L))
new_strat_array = strat_array.copy()
strat_array_t0 = strat_array.copy()

# Distribution fraction
t_variance = 0
omit_timesteps = 100
no_0 = np.zeros(timesteps-omit_timesteps)
no_1 = no_0.copy()
no_2 = no_0.copy()
no_3 = no_0.copy()
no_4 = no_0.copy()
no_5 = no_0.copy()
no_6 = no_0.copy()
no_7 = no_0.copy()

no_0[0] = np.count_nonzero(strat_array == 0)
no_1[0] = np.count_nonzero(strat_array == 1)
no_2[0] = np.count_nonzero(strat_array == 2)
no_3[0] = np.count_nonzero(strat_array == 3)
no_4[0] = np.count_nonzero(strat_array == 4)
no_5[0] = np.count_nonzero(strat_array == 5)
no_6[0] = np.count_nonzero(strat_array == 6)
no_7[0] = np.count_nonzero(strat_array == 7)


# Animation
fig1, ax1 = plt.subplots()
ims = []
im = ax1.imshow(strat_array_t0, vmin=0, vmax=N, animated=True)
ims.append([im])

for t in range(1,timesteps):

    P_array = np.zeros_like(strat_array)
    next_neighbor = np.roll(np.arange(L),-1)
    previous_neighbor = np.roll(np.arange(L),1)

    # Accumulate punishment for every agent i,j
    for i in range(L):
        for j in range(L):
 
            # Punishment for Von Neumann neighbors and self
            pSelf = play_game(strat_array[i,j], strat_array[i,j])
            pUp = play_game(strat_array[i,j], strat_array[previous_neighbor[i],j])
            pLeft = play_game(strat_array[i,j], strat_array[i,previous_neighbor[j]])
            pDown = play_game(strat_array[i,j], strat_array[next_neighbor[i],j])
            pRight = play_game(strat_array[i,j], strat_array[i,next_neighbor[j]])
            P_array[i,j] = pUp + pLeft + pDown + pRight
    
    # Compute new strategies for every agent
    for i in range(L):
        for j in range(L):

            r = np.random.uniform()
            if r < mu:
                new_strat_array[i,j] = np.random.randint(0,N+1)
            else:    
                agent_p = [P_array[i,j],P_array[next_neighbor[i],j],P_array[previous_neighbor[i],j],P_array[i,next_neighbor[j]],P_array[i,previous_neighbor[j]]]
                agent_strat = [strat_array[i,j],strat_array[next_neighbor[i],j],strat_array[previous_neighbor[i],j],strat_array[i,next_neighbor[j]],strat_array[i,previous_neighbor[j]]]
                new_strat_array[i,j] = np.random.choice([agent_strat[k] for k in range(len(agent_p)) if agent_p[k] == np.min(agent_p)])

            # pMin = np.argmin([P_array[i,j],P_array[next_neighbor[i],j],P_array[previous_neighbor[i],j],P_array[i,next_neighbor[j]],P_array[i,previous_neighbor[j]]])
            # if pMin == 0:
            #     new_strat_array[i,j] = strat_array[i,j]
            # if pMin == 1:
            #     new_strat_array[i,j] = strat_array[next_neighbor[i],j]
            # elif pMin == 2:
            #     new_strat_array[i,j] = strat_array[previous_neighbor[i],j]
            # elif pMin == 3:
            #     new_strat_array[i,j] = strat_array[i,next_neighbor[j]]
            # elif pMin == 4:
            #     new_strat_array[i,j] = strat_array[i,previous_neighbor[j]]

    strat_array = new_strat_array.copy()

    # Images for animation
    im = ax1.imshow(new_strat_array.copy(), vmin=0, vmax=N, animated=True)
    ims.append([im])

    if t >= omit_timesteps:
        no_0[t_variance] = np.count_nonzero(strat_array == 0)
        no_1[t_variance] = np.count_nonzero(strat_array == 1)
        no_2[t_variance] = np.count_nonzero(strat_array == 2)
        no_3[t_variance] = np.count_nonzero(strat_array == 3)
        no_4[t_variance] = np.count_nonzero(strat_array == 4)
        no_5[t_variance] = np.count_nonzero(strat_array == 5)
        no_6[t_variance] = np.count_nonzero(strat_array == 6)
        no_7[t_variance] = np.count_nonzero(strat_array == 7)
        t_variance += 1
print('R = {}, S = {}\n'.format(R,S))

# Mean and variance of the population
no_0_mean = np.sum(no_0) / len(no_0)
no_1_mean = np.sum(no_1) / len(no_1)
no_2_mean = np.sum(no_2) / len(no_2)
no_3_mean = np.sum(no_3) / len(no_3)
no_4_mean = np.sum(no_4) / len(no_4)
no_5_mean = np.sum(no_5) / len(no_5)
no_6_mean = np.sum(no_6) / len(no_6)
no_7_mean = np.sum(no_7) / len(no_7)

mean_array = np.round(np.array([no_0_mean, no_1_mean, no_2_mean, no_3_mean, no_4_mean, no_5_mean, no_6_mean, no_7_mean]),2)
[print(f'Mean strat. {i}: ', mean_array[i]) for i in range(len(mean_array))]
print('\n')

no_0_variance = np.sum((no_0-no_0_mean)**2) / len(no_0)
no_1_variance = np.sum((no_1-no_1_mean)**2) / len(no_1)
no_2_variance = np.sum((no_2-no_2_mean)**2) / len(no_2)
no_3_variance = np.sum((no_3-no_3_mean)**2) / len(no_3)
no_4_variance = np.sum((no_4-no_4_mean)**2) / len(no_4)
no_5_variance = np.sum((no_5-no_5_mean)**2) / len(no_5)
no_6_variance = np.sum((no_6-no_6_mean)**2) / len(no_6)
no_7_variance = np.sum((no_7-no_7_mean)**2) / len(no_7)

variance_array = np.round(np.array([no_0_variance, no_1_variance, no_2_variance, no_3_variance, no_4_variance, no_5_variance, no_6_variance, no_7_variance]), 2)
[print(f'Variance strat. {i}: ', variance_array[i]) for i in range(len(variance_array))]
variance_sum =np.sum(variance_array)
print('Variance sum: {}'.format(variance_sum))
print('\n')

deviation_array = np.round(variance_array**0.5, 2)
[print(f'Standard devation strat. {i}: ', deviation_array[i]) for i in range(len(deviation_array))]

fig1.colorbar(im, ax=ax1)
ani = animation.ArtistAnimation(fig1, ims, interval=50, blit=True)
writergif = animation.PillowWriter(fps=30) 
ani.save('exercise_13.5_R{}_S{}.gif'.format(R,S), writer=writergif)

fig2, ax2 = plt.subplots(figsize=(6,6))
title = 'L = {}, T = {}, R = {}, P = {}, S = {}, $\mu$ = {}'.format(L,T,R,P,S,mu)
ax2.set_title(title)
ax2.imshow(strat_array, vmin=0, vmax=N)
ax2.set_yticks(())
ax2.set_xticks(())
ax2.set_xlabel('$t$ = {}'.format(timesteps))
fig2.colorbar(im, ax=ax2)
plt.savefig('exercise_13.5_R{}_S{}.png'.format(R,S), bbox_inches='tight')

fig3, ax3 = plt.subplots(figsize=(6,6))
t_arange = np.arange(omit_timesteps,timesteps,1)
ax3.plot(t_arange, no_0/(L*L), label='Strat. 0')
ax3.plot(t_arange, no_1/(L*L), label='Strat. 1')
ax3.plot(t_arange, no_2/(L*L), label='Strat. 2')
ax3.plot(t_arange, no_3/(L*L), label='Strat. 3')
ax3.plot(t_arange, no_4/(L*L), label='Strat. 4')
ax3.plot(t_arange, no_5/(L*L), label='Strat. 5')
ax3.plot(t_arange, no_6/(L*L), label='Strat. 6')
ax3.plot(t_arange, no_7/(L*L), label='Strat. 7')
ax3.set_title(title)
ax3.set_xlabel('$t$')
ax3.set_ylabel('Population fraction')
plt.legend(loc="upper left",fontsize=8)
plt.savefig('exercise_13.5_PF_R{}_S{}.png'.format(R,S), bbox_inches='tight')

plt.show()