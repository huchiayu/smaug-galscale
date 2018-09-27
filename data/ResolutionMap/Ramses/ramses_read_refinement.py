import matplotlib.pylab as plt
import numpy as np
import math
import glob

def main():
	resolutionFilenames = glob.glob('*_resolution_*.dat')

	for filename in resolutionFilenames:
		data = read_data(filename)
		filenameshort = filename[:-4] #strip the filenames of the '.dat' extension
		plot_data(data, filenameshort)

def read_data(filename, boxsize=60):

	data = np.loadtxt(filename)

	levels = data[:,2]
	resolutions = np.ones(levels.shape)*boxsize / (2**levels) * 1000
	size = int(math.sqrt(resolutions.shape[0]))
	resolutions = resolutions.reshape(size, size)

	return resolutions

def plot_data(data, filename, boxsize=60, x_min=-5., x_max=5., y_min=-5., y_max=5., v_min=7, v_max=200, cmap='viridis', plotLog=True):

    fig, ax = plt.subplots(1, 1, figsize=(10,8))
    label = 'resolution [pc]'
    res_ticks=[60*2**_i for _i in range(-13, 7)]
 
    if plotLog:
        data = np.log10(data)
        v_min = math.log10(v_min)
        v_max = math.log10(v_max)
        res_ticks=[math.log10(boxsize*1000*2**_i) for _i in range(-13, -7)]

    CS = ax.imshow(data, cmap=cmap, aspect='equal', extent=(x_min, x_max, y_min, y_max), vmin=v_min, vmax=v_max, origin='lower')

    cbar = fig.colorbar(CS, label=label, ticks=res_ticks)
    
    if plotLog:
        res_ticklabels = ['{:.2f}'.format(10**tick) for tick in res_ticks]
        cbar.ax.set_yticklabels(res_ticklabels)
    
    ax.set_xlabel('$x\ \mathrm{[kpc]}$')
    ax.set_ylabel('$y\ \mathrm{[kpc]}$')

    fig.savefig("./figs/{}.png".format(filename))



if __name__ == '__main__':
    main()
