import matplotlib.pylab as plt
import numpy as np
import glob

def main():

	#Find all files containing SFR data
	filenames = glob.glob('ramses_*_SFR.dat')
	#Alternatively, you can also manually provide a list of files:
	#filenames = ['wlm_ramses_SF_FB_sfr.dat']

	for filename in filenames:

		times, sfrs = read_sfr(filename)
		filenameshort = filename[:-4]
		plot_sfr(times, sfrs, filenameshort)


def plot_sfr(times, sfrs, filename, x_min=0., x_max=1., y_min=1e-4, y_max=10**-0.5):

	fig, ax1 = plt.subplots(1, 1, figsize=(7,5))

	ax1.plot(times, sfrs, 'r-', color='b')

	ax1.set_yscale('log')
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.set_xlabel('$t\ \mathrm{[Gyr]}$')
	ax1.set_ylabel('$\mathrm{SFR}\ \mathrm{[M_\odot/yr]}$')

	fig.savefig('./figs/{}.png'.format(filename))
	

def read_sfr(filename):

	readfile = np.loadtxt(filename)

	times = [r[0] for r in readfile[:101]]
	sfrs = [r[1] for r in readfile[:101]]

	return times, sfrs

if __name__ == '__main__':
    main()

