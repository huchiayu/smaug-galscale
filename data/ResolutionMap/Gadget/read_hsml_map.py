import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt

Npix = 300

filename = "./hsml_map_wFB_500.txt"
hsmlMap_wFB_500 = np.loadtxt(filename)
hsmlMap_wFB_500 = hsmlMap_wFB_500.reshape(Npix,Npix)

filename = "./hsml_map_noFB_500.txt"
hsmlMap_noFB_500 = np.loadtxt(filename)
hsmlMap_noFB_500 = hsmlMap_noFB_500.reshape(Npix,Npix)

filename = "./hsml_map_wFB_1000.txt"
hsmlMap_wFB_1000 = np.loadtxt(filename)
hsmlMap_wFB_1000 = hsmlMap_wFB_1000.reshape(Npix,Npix)

filename = "./hsml_map_noFB_1000.txt"
hsmlMap_noFB_1000 = np.loadtxt(filename)
hsmlMap_noFB_1000 = hsmlMap_noFB_1000.reshape(Npix,Npix)


extent = [-5,5,-5,5]


plt.subplot(221)
plt.title('t=500 Myr, wFB')
plt.imshow(np.log10(hsmlMap_wFB_500), extent=extent, interpolation=None, cmap='viridis', origin='lower', vmin=-3, vmax=0)
plt.colorbar()
plt.subplot(222)
plt.title('t=500 Myr, noFB')
plt.imshow(np.log10(hsmlMap_noFB_500), extent=extent, interpolation=None, cmap='viridis', origin='lower', vmin=-3, vmax=0)
plt.colorbar()
plt.subplot(223)
plt.title('t=1000 Myr, wFB')
plt.imshow(np.log10(hsmlMap_wFB_1000), extent=extent, interpolation=None, cmap='viridis', origin='lower', vmin=-3, vmax=0)
plt.colorbar()
plt.subplot(224)
plt.title('t=1000 Myr, noFB')
plt.imshow(np.log10(hsmlMap_noFB_1000), extent=extent, interpolation=None, cmap='viridis', origin='lower', vmin=-3, vmax=0)
plt.colorbar()
plt.show()

