import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

# Leer los datos del archivo

data   = np.loadtxt('electronica_industrial/buck_mod_12kw.csv', skiprows=1, delimiter=',')

# 30°
t_v   = data[:len(data)//2, 0]
v1_v  = data[:len(data)//2, 1]
v2r_v = data[:len(data)//2, 2]
vL_v  = data[:len(data)//2, 3]
iL_v  = data[:len(data)//2, 4]
vo_v  = data[:len(data)//2, 5]
io_v  = data[:len(data)//2, 6]

for i in range(0,len(t_v)):
    t_v[i] = (t_v[i] - 0.2) * 1e6

# Calculo de RMS y media

vo_av  = np.mean(vo_v) # Valor medio de V_L
io_av  = np.mean(io_v) # Valor medio de I_L
vo_rms = np.sqrt(np.mean(vo_v ** 2)) # Valor RMS de V_L
io_rms = np.sqrt(np.mean(io_v ** 2)) # Valor RMS de I_L

print('promedio: ', vo_av, ' V; ', io_av, 'A')
print('rms: ', vo_rms, ' V; ', io_rms, 'A')

# Graficos

# -------------------------------
    
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, sharex=True, figsize=(6,6))

ax1.plot(t_v, v1_v , color='b', linewidth=1, linestyle='-', label=r'$v_{1}$')
ax1.plot(t_v, v2r_v, color='g', linewidth=1, linestyle='-', label=r'$v_{2}/N$')
ax1.plot(t_v, vL_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$v_{L}$')
ax2.plot(t_v, iL_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$i_{L}$')
ax3.plot(t_v, vo_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$v_{o}$')
ax4.plot(t_v, io_v , color='r', linewidth=1.5  , linestyle='-' , label=r'$i_{o}$')

ax1.set_ylabel('[V]')
ax1.legend(loc='upper right')
ax1.grid(True)
ax1.yaxis.set_major_locator(MultipleLocator(50))

ax2.set_ylabel('[A]')
ax2.legend(loc='upper right')
ax2.grid(True)
ax2.yaxis.set_major_locator(MultipleLocator(80))

ax3.set_ylabel('[V]')
ax3.legend(loc='upper right')
ax3.grid(True)
ax3.set_ylim(-max(vo_v)*0.1, max(vo_v)*1.1)
# ax3.yaxis.set_major_locator(MultipleLocator(100)) # Boost
ax3.yaxis.set_major_locator(MultipleLocator(48)) # Buck

ax4.set_ylabel('[A]')
ax4.legend(loc='upper right')
ax4.grid(True)
ax4.set_ylim(-max(io_v)*0.1, max(io_v)*1.1)
# ax4.yaxis.set_major_locator(MultipleLocator(10)) # Boost
ax4.yaxis.set_major_locator(MultipleLocator(250)) # Buck 12kW
# ax4.yaxis.set_major_locator(MultipleLocator(333)) # Buck 16kW
ax4.set_xlabel('Tiempo [us]')

plt.show()