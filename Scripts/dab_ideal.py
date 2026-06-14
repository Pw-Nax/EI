import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

data   = np.loadtxt('electronica_industrial/tpt9.csv', skiprows=1, delimiter=',')

N = 50
periods = 5
delay = 20

V1 = 1
V2 = 1
G = 1
Vi = V1
Vo = V2 * G
n = V2 / V1

# f = 40e3
# L = 1.8e-6
f = 1
L = 1
w = 2 * np.pi * f

q14_v = np.concatenate([np.ones(N), np.zeros(N)] * periods)
q23_v = np.concatenate([np.zeros(N), q14_v[:-N]])
q58_v = np.concatenate([np.zeros(delay), q14_v[:-delay]])
q67_v = np.concatenate([np.ones(delay), q23_v[:-delay]])

v1_v = 2*Vi * q14_v - Vi
vor_v = 2 * Vo/n * q58_v - Vo/n
vL_v = v1_v - vor_v

iL_v = (np.cumsum(vL_v) - np.average(np.cumsum(vL_v))) / 20
IL = np.max(iL_v)

# print(q58_v)

t_v = np.arange(len(q14_v)) / (2*N)

fig, (ax1,ax2,ax3) = plt.subplots(3,1, sharex=True, figsize=(10, 5))

ax1.plot(t_v, v1_v, label=r'$v_p$')
ax1.plot(t_v, vor_v, label=r'$v_s/n$')
# ax1.set_ylabel(r'x $V_p$')
ax1.set_yticks([-V1, 0, V1])
ax1.set_yticklabels([r'$-V_p$', '0', '$V_p$'])
ax1.grid()
ax1.legend(loc='upper right')

ax2.plot(t_v, vL_v, label=r'$v_L$')
ax2.set_yticks([-2*V1, 0, 2*V1])
ax2.set_yticklabels([r'$-2V_p$', '0', '$2V_p$'])
ax2.grid()
ax2.legend(loc='upper right')

ax3.plot(t_v, iL_v, label=r'$i_L$')
ax3.set_yticks([-IL, 0, IL])
ax3.set_yticklabels([r'$-I_L$', '0', '$I_L$'])
ax3.grid()
ax3.legend(loc='upper right')
ax3.set_xlabel('Períodos de conmutación (T)')

# -------------------------------

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, sharex=True, figsize=(10, 3))

ax1.plot(t_v, q14_v, label=r'$v_{G14}$')
ax1.set_yticks([0, 1])
ax1.set_yticklabels(['0', '$V_g$'])
ax1.grid()
ax1.legend(loc='upper right')

ax2.plot(t_v, q23_v, label=r'$v_{G23}$')
ax2.set_yticks([0, 1])
ax2.set_yticklabels(['0', '$V_g$'])
ax2.grid()
ax2.legend(loc='upper right')

ax3.plot(t_v, q58_v, color="#FF9100", label=r'$v_{G58}$')
ax3.set_yticks([0, 1])
ax3.set_yticklabels(['0', '$V_g$'])
ax3.grid()
ax3.legend(loc='upper right')

ax4.plot(t_v, q67_v, color='#FF9100', label=r'$v_{G67}$')
ax4.set_yticks([0, 1])
ax4.set_yticklabels(['0', '$V_g$'])
ax4.grid()
ax4.legend(loc='upper right')
# ax4.set_xlabel('Períodos de conmutación (T)')

plt.show()





# # Graficos

# # -------------------------------
    
# fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, sharex=True)

# # acel: 148000,149000
# # freno: 

# ax1.plot(t_v[140000:220000], vg1_v[140000:220000], color='r', linewidth=1, linestyle='-', label=r'$v_{G1}$')
# ax1.plot(t_v[140000:220000], vg2_v[140000:220000], color='g', linewidth=1, linestyle='-', label=r'$v_{G2}$')

# ax2.plot(t_v[140000:220000], vl_v[140000:220000], color='r', linewidth=1, linestyle='-', label=r'$v_{L}$')
# ax3.plot(t_v[140000:220000], ia_v[140000:220000], color='g', linewidth=1, linestyle='-', label=r'$i_{a}$')
# ax4.plot(t_v[140000:220000], n_v[140000:220000], color='b', linewidth=1, linestyle='-', label=r'$n$')

# ax1.set_ylabel('[V]')
# ax1.legend()
# ax1.grid(True)
# # ax1.yaxis.set_major_locator(MultipleLocator(25))

# ax2.set_ylabel('[V]')
# ax2.legend()
# ax2.grid(True)
# ax2.yaxis.set_major_locator(MultipleLocator(90))

# ax3.set_ylabel('[A]')
# ax3.legend()
# ax3.grid(True)
# # ax3.set_ylim(-1,3)
# # ax3.yaxis.set_major_locator(MultipleLocator(40))

# ax4.set_ylabel('[rpm]')
# ax4.legend()
# ax4.grid(True)
# # ax4.set_ylim(-10,100)
# # ax4.yaxis.set_major_locator(MultipleLocator(40))
# ax4.set_xlabel('Tiempo [s]')

# plt.show()