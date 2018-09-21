import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt


Npix = 300

filename = "./surfaceDensityMap_wFB_000.txt"
sdmap_wFB_000 = np.loadtxt(filename)
sdmap_wFB_000 = sdmap_wFB_000.reshape(Npix,Npix)

filename = "./surfaceDensityMap_wFB_500.txt"
sdmap_wFB_500 = np.loadtxt(filename)
sdmap_wFB_500 = sdmap_wFB_500.reshape(Npix,Npix)

filename = "./surfaceDensityMap_wFB_1000.txt"
sdmap_wFB_1000 = np.loadtxt(filename)
sdmap_wFB_1000 = sdmap_wFB_1000.reshape(Npix,Npix)

filename = "./surfaceDensityMap_noFB_000.txt"
sdmap_noFB_000 = np.loadtxt(filename)
sdmap_noFB_000 = sdmap_noFB_000.reshape(Npix,Npix)

filename = "./surfaceDensityMap_noFB_500.txt"
sdmap_noFB_500 = np.loadtxt(filename)
sdmap_noFB_500 = sdmap_noFB_500.reshape(Npix,Npix)

filename = "./surfaceDensityMap_noFB_1000.txt"
sdmap_noFB_1000 = np.loadtxt(filename)
sdmap_noFB_1000 = sdmap_noFB_1000.reshape(Npix,Npix)

extent = [-5,5,-5,5]

plt.subplot(221)
plt.imshow(sdmap_wFB_000.T, extent=extent, interpolation=None, cmap='viridis', origin='lower')
plt.colorbar()
plt.subplot(222)
plt.imshow(sdmap_wFB_500.T, extent=extent, interpolation=None, cmap='viridis', origin='lower')
plt.colorbar()
plt.subplot(223)
plt.imshow(sdmap_wFB_1000.T, extent=extent, interpolation=None, cmap='viridis', origin='lower')
plt.colorbar()
plt.show()


