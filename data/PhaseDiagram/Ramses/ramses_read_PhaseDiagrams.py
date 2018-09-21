import matplotlib.pylab as plt
import numpy as np
import glob

def main():

	#Find all files containing rho_Tmu data
	PhaseDiagramFilenames = glob.glob('*_PhaseDiagram_*.dat')
	#Alternatively, you can also manually provide a list of files
	#PhaseDiagramFilenames = ['ramses_cooling_PhaseDiagram_1000.dat', 'ramses_cooling_SF_noFB_PhaseDiagram_0500.dat']

	for filename in PhaseDiagramFilenames:
		#Read and plot the file with rho_Tmu data 
		rho_Tmu = read_data(filename)
		filenameshort = filename[:-4] #strip the filenames of the '.dat' extension
		plot_data(rho_Tmu, filenameshort, y_min=0., y_max=8.)
		#plot_1dhistograms(rho_Tmu, filenameshort, y_min=0., y_max=8.)

	#Do the same for the files with pressure instead of T/mu
	PnPDFilenames = glob.glob('*_PnPD_*.dat')
	for filename in PnPDFilenames:
		#Read and plot the file with rho_Tmu data 
		PnPD = read_data(filename)
		filenameshort = filename[:-4] #strip the filenames of the '.dat' extension
		plot_data(PnPD, filenameshort)
		#plot_1dhistograms(PnPD, filenameshort)

def read_data(filename):

	data = np.loadtxt(filename)
	np.flip(data, 0)

	return data


def plot_data(data, filename, x_min=-6., x_max=4., y_min=-4., y_max=5., v_min=-2, v_max=7, resolution=128, cmap='viridis'):

	fig, ax = plt.subplots(1, 1, figsize=(10,8))
	CS = ax.imshow(np.log10(data), cmap=cmap, aspect='equal', extent=(x_min, x_max, y_min, y_max), vmin=v_min, vmax=v_max, origin='lower')

	cbar = fig.colorbar(CS, label='$\log_{10}(M/\mathrm{M_\odot})$')

	if 'PnPD' in filename: 
		ax.set_xlabel('$\log_{10}(\\rho/m_p)\ \mathrm{[cm^{-3}]}$')
		ax.set_ylabel('$\log_{10}(P/k_b)\ \mathrm{[K\ cm^{-3}]}$')
	elif 'PhaseDiagram' in filename:
		ax.set_xlabel('$\log_{10}(\\rho/m_p)\ \mathrm{[cm^{-3}]}$')
		ax.set_ylabel('$\log_{10}(T/\mu)\ \mathrm{[K]}$')

	fig.savefig("./figs/{}.png".format(filename))

def plot_1dhistograms(data, filename, x_min=-6., x_max=4., y_min=-4., y_max=5., resolution=128, logPlot=False):
	#Quick and dirty routine to project the 2D grids on both their axes, given 1D histograms of density and pressure or T/mu.
	x_hist = [sum(data[:,_i]) for _i in range(len(data[0]))]
	y_hist = [sum(d) for d in data]

	if logPlot:
		x_hist = np.log10(x_hist)
		y_hist = np.log10(y_hist)

	fig1, ax1 = plt.subplots(1, 1, figsize=(8,5))
	x_range = np.linspace(x_min, x_max, num=resolution, endpoint=True)

	ax1.plot(x_range, x_hist)
	ax1.set_xlim(x_min, x_max)
	ax1.set_xlabel('$\log_{10}(\\rho/m_p)\ \mathrm{[cm^{-3}]}$')

	if logPlot:
		ax1.set_ylabel('$\log_{10}(M/\mathrm{M_\odot})$')
	else:
		ax1.set_ylabel('$M/\mathrm{M_\odot}$')
	
	fig1.savefig('./figs/{}_densityHistogram.png'.format(filename))

	fig2, ax2 = plt.subplots(1, 1, figsize=(8,5))
	y_range = np.linspace(y_min, y_max, num=resolution, endpoint=True)
	ax2.plot(y_range, y_hist)
	ax2.set_xlim(y_min, y_max)
	if logPlot:
		ax2.set_ylabel('$\log_{10}(M/\mathrm{M_\odot})$')
	else:
		ax2.set_ylabel('$M/\mathrm{M_\odot}$')

	if 'PnPD' in filename: 
		ax2.set_xlabel('$\log_{10}(P/k_b)\ \mathrm{[K\ cm^{-3}]}$')
		fig2.savefig('./figs/{}_pressureHistogram.png'.format(filename))
	elif 'PhaseDiagram' in filename:
		ax2.set_xlabel('$\log_{10}(T/\mu)\ \mathrm{[K]}$')
		fig2.savefig('./figs/{}_TmuHistogram.png'.format(filename))

if __name__ == '__main__':
    main()

