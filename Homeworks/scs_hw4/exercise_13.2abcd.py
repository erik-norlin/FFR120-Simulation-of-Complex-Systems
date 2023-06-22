# Exercise 13.2abcd
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
R = 0.99
P = 1
S = 1.5
mu = 0
timesteps = 20

L = 30
strat_array = np.ones((L,L))*0
strat_array[int(L/2),int(L/2)] = N
# strat_array[int(2*L/5),int(2*L/5)] = 0
# strat_array[int(-L/5),int(-L/5)] = 0
# strat_array[int(-2*L/5),int(-2*L/5)] = 0
# strat_array[int(L/5),int(L/5)] = 0
new_strat_array = strat_array.copy()
strat_array_t0 = strat_array.copy()

# Animation
fig1, ax = plt.subplots()
ims = []
im = ax.imshow(strat_array_t0)
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
                new_strat_array[i,j] = np.random.choice([0,N])
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
    im = ax.imshow(new_strat_array.copy(), animated=True)
    ims.append([im])

fig, axs = plt.subplots(1,2,figsize=(7,7))
title = 'One defector, lattice size = {}, T = {}, R = {}, P = {}, S = {}, $\mu$ = {}'.format(L,T,R,P,S,mu)

axs[0].set_title(title, loc='left')
axs[0].imshow(strat_array_t0)
axs[0].set_yticks(())
axs[0].set_xticks(())
axs[0].set_xlabel('$t$ = 0')

axs[1].imshow(strat_array)
axs[1].set_yticks(())
axs[1].set_xticks(())
axs[1].set_xlabel('$t$ = {}'.format(timesteps))

ani = animation.ArtistAnimation(fig1, ims, interval=5, blit=True)
writergif = animation.PillowWriter(fps=30) 
# ani.save('exercise_13.2_1def_R{}.gif'.format(R), writer=writergif)

# plt.savefig('exercise_13.2_1def_R{}.png'.format(R), bbox_inches='tight')
plt.show()





