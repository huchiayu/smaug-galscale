import numpy as np
import math
import matplotlib.pyplot as plt
from plotEquilPD import plotEquilPD
import itertools

def compare_PDF(num, fb=True, sf=True, cooling=True):

    fig = plt.figure(figsize=(10, 9))

    if(fb==False):
        codename=['gadget', 'ramses', 'enzo']
        dirname=['Gadget/', 'Ramses/', 'Enzo/']
    else:
        codename=['gadget', 'ramses']
        dirname=['Gadget/', 'Ramses/']

    for (code, dir) in zip(codename, dirname):

        if(fb==True):
            physics = '_cooling_SF_FB'
        elif(sf==True):
            physics = '_cooling_SF_noFB'
        elif(cooling==True):
            physics = '_cooling'
        else:
            physics = '_adiabatic'

        #if(code=='enzo'):
        #    physics = '_cooling'


        filename = dir + code + physics + '_PhaseDiagram_' + num + '.dat'
        data = np.loadtxt(filename)
        data = data.reshape(128,128)
        if(code!='ramses'):
            data = data.T
        if(code=='gadget'):
            data*=100. #100 M_sol per particle

        rhobin = np.linspace(-6,4,129)
        Tbin = np.linspace(0,8,129)

        print code, codename
        plt.subplot(2, 2, 1)
        plt.plot( (rhobin[1:]+rhobin[:-1])/2., np.sum(data,0), '-', label=code)
        plt.yscale('log')
        plt.xlabel(r'$\log_{10} \rho/m_p [cm^{-3}]$', fontsize=13)
        plt.legend(loc='lower right', fontsize=13)

        plt.subplot(2, 2, 3)
        plt.plot( (rhobin[1:]+rhobin[:-1])/2., np.cumsum( np.sum(data,0) ), '-')
        plt.yscale('log')
        plt.xlabel(r'$\log_{10} \rho/m_p [cm^{-3}]$', fontsize=13)

        plt.subplot(2, 2, 2)
        plt.plot( (Tbin[1:]+Tbin[:-1])/2., np.sum(data,1), '-')
        plt.yscale('log')
        plt.xlabel(r'$\log_{10} T/\mu [K]$', fontsize=13)

        plt.subplot(2, 2, 4)
        plt.plot( (Tbin[1:]+Tbin[:-1])/2., np.cumsum( np.sum(data,1) ), '-')
        plt.yscale('log')
        plt.xlabel(r'$\log_{10} T/\mu [K]$', fontsize=13)

    plt.show()

def plot_PD(code='gadget', fb=True, sf=True, cooling=True):

    num = ['0000', '0500', '1000', '1500']

    xmin = -6
    xmax = 4
    ymin = 0
    ymax = 8
    extent = [xmin, xmax, ymin, ymax]
    
    fig = plt.figure(figsize=(10, 9))
    
    snaps=[0, 1, 2, 3]
    dir=''
    if(code=='ramses'):
        dir='Ramses/'
        if(fb==True):
            snaps=[0, 1]

    if(code=='enzo'):
        dir='Enzo/'
        if(sf==True):
            snaps=[0, 1]
        else:
            snaps=[0, 1, 2]

    if(code=='gadget'):
        dir='Gadget/'


    for i in snaps:
        if(fb==True):
            physics = '_cooling_SF_FB'
        elif(sf==True):
            physics = '_cooling_SF_noFB'
        elif(cooling==True):
            physics = '_cooling'
        else:
            physics = '_adiabatic'

        filename = dir + code + physics + '_PhaseDiagram_' + num[i] + '.dat'

        data = np.loadtxt(filename)
        data = data.reshape(128,128)
        if(code!='ramses'):
            data = data.T

        plt.subplot(2, 2, i+1)
        plt.imshow(np.log10(data), extent=extent, interpolation=None, cmap='viridis', origin='lower')
        plt.axis([xmin,xmax,ymin,ymax])
        plt.yticks(range(ymin,ymax), fontsize=13)
        plt.ylabel(r'$\log_{10} T/\mu [K]$', fontsize=13)
        plt.xticks(range(xmin,xmax), fontsize=13)
        plt.xlabel(r'$\log_{10} \rho/m_p [cm^{-3}]$', fontsize=13)
        plotEquilPD(num[i])
        
        plt.text(-4, 7, 'time = ' + num[i] + 'Myr', fontsize=13, rotation=0)
        if(i==0):
            plt.text(1, 9, code+physics, fontsize=15, rotation=0)

    plt.show()


if __name__ == '__main__':
    plot_PD(fb=False)


