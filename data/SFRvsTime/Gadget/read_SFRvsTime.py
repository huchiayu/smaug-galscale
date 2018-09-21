import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt



filename = "./SFRvsTime_noFB.txt"
time, SFR_noFB = np.loadtxt(filename)

filename = "./SFRvsTime_wFB.txt"
time, SFR_wFB = np.loadtxt(filename)

plt.plot(time,SFR_wFB)
plt.plot(time,SFR_noFB)
plt.yscale('log')
plt.show()


