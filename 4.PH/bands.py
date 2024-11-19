import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../src/GaAs-phonon/GaAs.freq.gp")

nbands = data.shape[1] - 1
for band in range(nbands):
    plt.plot(data[:, 0], data[:, band], linewidth=1, alpha=0.5, color='k')
# High symmetry k-points (check matdyn.GaAs.in)
plt.axvline(x=data[0, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[20, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[40, 0], linewidth=0.5, color='k', alpha=0.5)
plt.axvline(x=data[60, 0], linewidth=0.5, color='k', alpha=0.5)
plt.xticks(ticks= [0, data[20, 0], data[40, 0], data[60, 0], data[-1, 0]], \
           labels=['L', '$\Gamma$', 'X', 'U,K', '$\Gamma$'])
plt.ylabel("Frequency (cm$^{-1}$)")
plt.xlim(data[0, 0], data[-1, 0])
plt.ylim(0, )
plt.show()
