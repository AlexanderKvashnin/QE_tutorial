import numpy as np
import matplotlib.pyplot as plt

freq, dos, pdos_Ga, pdos_As = np.loadtxt("GaAs.dos", unpack=True)

plt.plot(freq, dos, c='k', lw=0.5, label='Total')
plt.plot(freq, pdos_Ga, c='b', lw=0.5, label='Ga')
plt.plot(freq, pdos_As, c='r', lw=0.5, label='As')
plt.xlabel('$\\Omega~(cm^{-1}$)')
plt.ylabel('Phonon DOS (state/cm$^{-1}/u.c.$)')
plt.legend(frameon=False, loc='upper left')
plt.xlim(freq[0], freq[-1])
plt.savefig('dos.png', dpi=150)
plt.show()
