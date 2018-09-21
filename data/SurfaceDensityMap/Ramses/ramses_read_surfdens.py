import matplotlib.pylab as plt
import numpy as np
import glob

def main():

	#Find all files containing surface density data
	filenames = glob.glob('*_SurfaceDensity*.dat')
	#Alternatively, you can also manually provide a list of files
	#filenames = ['wlm_ramses_SF_FB_0.5Gyr_faceon_surfdens.dat']

	for filename in filenames:
		#Read and plot the file with surface density data 
		surfdens = read_surfdens(filename)
		filenameshort = filename[:-4]
		plot_surfdens(surfdens, filenameshort)


def plot_surfdens(surfdens, filename, x_min=-5., x_max=5., y_min=-5., y_max=5., v_min=-1.5, v_max=1.5, cmap='viridis'):

	fig, ax = plt.subplots(1, 1, figsize=(10,8))
	CS = ax.imshow(np.log10(surfdens), cmap=cmap, aspect='equal', extent=(x_min, x_max, y_min, y_max), vmin=v_min, vmax=v_max, origin='lower')

	cbar = fig.colorbar(CS, label='$\log_{10}(\Sigma)\ \mathrm{[M_\odot\ pc^{-2}]}$')

	ax.set_xlabel('$x\ \mathrm{[kpc]}$')
	ax.set_ylabel('$y\ \mathrm{kpc}$')

	fig.savefig("./figs/{}.png".format(filename))


def read_surfdens(filename):

	surfdens = np.loadtxt(filename)
	np.flip(surfdens, 0)

	return surfdens

if __name__ == '__main__':
    main()

