# Exercise 13.4abcd
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
R = 0.65
P = 1
S = 1.5
mu = 0.01
timesteps = 300

L = 30
strat_array = np.random.randint(0,N+1,size=(L,L))
new_strat_array = strat_array.copy()
strat_array_t0 = strat_array.copy()

# Distribution fraction
no_0 = np.zeros(timesteps)
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

    no_0[t] = np.count_nonzero(strat_array == 0)
    no_1[t] = np.count_nonzero(strat_array == 1)
    no_2[t] = np.count_nonzero(strat_array == 2)
    no_3[t] = np.count_nonzero(strat_array == 3)
    no_4[t] = np.count_nonzero(strat_array == 4)
    no_5[t] = np.count_nonzero(strat_array == 5)
    no_6[t] = np.count_nonzero(strat_array == 6)
    no_7[t] = np.count_nonzero(strat_array == 7)

fig1.colorbar(im, ax=ax1)
ani = animation.ArtistAnimation(fig1, ims, interval=50, blit=True)
writergif = animation.PillowWriter(fps=30) 
ani.save('exercise_13.4_R{}.gif'.format(R), writer=writergif)

fig2, ax2 = plt.subplots(figsize=(6,6))
title = 'L = {}, T = {}, R = {}, P = {}, S = {}, $\mu$ = {}'.format(L,T,R,P,S,mu)
ax2.set_title(title)
ax2.imshow(strat_array, vmin=0, vmax=N)
ax2.set_yticks(())
ax2.set_xticks(())
ax2.set_xlabel('$t$ = {}'.format(timesteps))
fig2.colorbar(im, ax=ax2)
plt.savefig('exercise_13.4_R{}.png'.format(R), bbox_inches='tight')

fig3, ax3 = plt.subplots(figsize=(6,6))
t_linspace = np.linspace(0,timesteps,timesteps)
ax3.plot(t_linspace, no_0/(L*L), label='Strat. 0')
ax3.plot(t_linspace, no_1/(L*L), label='Strat. 1')
ax3.plot(t_linspace, no_2/(L*L), label='Strat. 2')
ax3.plot(t_linspace, no_3/(L*L), label='Strat. 3')
ax3.plot(t_linspace, no_4/(L*L), label='Strat. 4')
ax3.plot(t_linspace, no_5/(L*L), label='Strat. 5')
ax3.plot(t_linspace, no_6/(L*L), label='Strat. 6')
ax3.plot(t_linspace, no_7/(L*L), label='Strat. 7')
ax3.set_title(title)
ax3.set_xlabel('$t$')
ax3.set_ylabel('Population fraction')
plt.legend(loc="upper left",fontsize=8)
plt.savefig('exercise_13.4_PF_R{}.png'.format(R), bbox_inches='tight')

plt.show()

# The larger R is (punishment for cooperation) the more the population defects.
# The smaller R is, the more the population cooperates.
# Stable strategies are: defect every time, cooperate almost all the time to all the time. 
# Which strategy that will become stable depends on R.
# Cooperation and defection fluctuates past each other continiously if R is "right in between".