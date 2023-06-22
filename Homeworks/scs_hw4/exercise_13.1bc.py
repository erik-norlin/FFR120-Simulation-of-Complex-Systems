# Exercise 13.1bc
import numpy as np
import matplotlib.pyplot as plt
import sys

N = 10
T = 0
R = 0.5
P = 1
S = 1.5
m_strats = np.linspace(0,N,N+1)
n_strats = np.linspace(0,N,N+1)
no_years_array = np.zeros((N+1, N+1))
coop = True
defect = False

for m_strat in m_strats:
    for n_strat in n_strats:

        m_previous = coop
        n_previous = coop
        no_years = 0

        for round in range(1,N+1):

            if round <= n_strat and m_previous == coop:
                n = coop
            else:
                n = defect

            if round <= m_strat and n_previous == coop:
                m = coop
            else:
                m = defect

            if n == coop and m == coop:
                no_years += R
            elif n == coop and m == defect:
                no_years += S
            elif n == defect and m == coop:
                no_years += T
            elif n == defect and m == defect:
                no_years += P

            n_previous = n
            m_previous = m

        no_years_array[int(n_strat), int(m_strat)] = no_years

fig,ax = plt.subplots(figsize=(6,6))
x,y = np.meshgrid(m_strats, n_strats)
years_min, years_max = no_years_array.min(), no_years_array.max()
map = ax.pcolormesh(x, y, no_years_array, cmap='RdBu', vmin=years_min, vmax=years_max)
fig.colorbar(map, ax=ax)


# ax.plot(n_strats, no_years_array, 'o', markersize=10)
# ax.plot([m_strat,m_strat], [4,10], '--', color='black', label='Strategy for m')
ax.set_title('Years in prison')
ax.set_xlabel('$m$')
ax.set_ylabel('$n$')
ax.set_box_aspect(1)

# plt.legend(loc="lower left",fontsize=8)
plt.savefig('exercise_13.1c_R' + str(R) + '_S' + str(S) + '.png', bbox_inches='tight')
plt.show()