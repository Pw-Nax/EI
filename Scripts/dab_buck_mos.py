import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

# Leer los datos del archivo

data   = np.loadtxt('electronica_industrial/buck_mos_3kw.csv', skiprows=1, delimiter=',')

# 30°
t_v   = data[:len(data)//2, 0]
vL_v  = data[:len(data)//2, 1]
i14_v  = data[:len(data)//2, 2]
i23_v  = data[:len(data)//2, 3]
i58_v  = data[:len(data)//2, 4]
i67_v  = data[:len(data)//2, 5]

for i in range(0,len(t_v)):
    t_v[i] = (t_v[i] - 0.5) * 1e6

# Graficos

# -------------------------------
    
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, sharex=True, figsize=(6,6))

ax2.plot(t_v, vL_v  , color='r', linewidth=1.5  , linestyle='-' , label=r'$v_{L}$')
ax3.plot(t_v, i14_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$i_{Q14}$')
ax3.plot(t_v, i23_v , color='b', linewidth=1.5  , linestyle='-' , label=r'$i_{Q23}$')
ax4.plot(t_v, i58_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$i_{Q58}$')
ax4.plot(t_v, i67_v , color='b', linewidth=1.5  , linestyle='-' , label=r'$i_{Q67}$')

ax2.set_ylabel('[V]')
ax2.legend(loc='upper right')
ax2.grid(True)
# ax1.yaxis.set_major_locator(MultipleLocator(50))

ax3.set_ylabel('[A]')
ax3.legend(loc='upper right')
ax3.grid(True)
ax3.yaxis.set_major_locator(MultipleLocator(167))
# ax3.yaxis.set_major_locator(MultipleLocator(83))

ax4.set_ylabel('[A]')
ax4.legend(loc='upper right')
ax4.grid(True)
# ax3.set_ylim(-max(io_v)*0.1, max(io_v)*1.1)
# ax3.yaxis.set_major_locator(MultipleLocator(63))
ax4.set_xlabel('Tiempo [us]')

plt.show()