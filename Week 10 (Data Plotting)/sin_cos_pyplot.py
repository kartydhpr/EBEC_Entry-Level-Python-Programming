################################################################################
# Author: Karteikay Dhuper
# Date: April 18th 2021
# Description This program generates a sin and cosine graph using matplotlib and
# distinguishes between them by color
################################################################################
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

def main():

    # plot initialization
    fig, ax = plt.subplots()

    # variable declaration
    xrange = np.arange(0,2*np.pi,0.01) # specifies the range for the x spine as 0 - 2pi with an increment of 0.1 radians
    sinValues = np.sin(xrange)
    cosineValues = np.cos(xrange)

    # plot manipulation
    plt.plot(xrange,sinValues, color = 'red')
    plt.plot(xrange,cosineValues, color = 'blue')
    ax.set_yticks([-1,1]) # specifies ticks for the y axis
    ax.set_xticks([1.6,3.2,4.7,6.3]) # specifies ticks for the x axis
    #ax.set_xlim(0,6.5)

    # ticker submodule function that formats ticks
    ax.xaxis.set_major_formatter(tck.FormatStrFormatter(r'$\pi/2$'))

    # spine (axis + border) manipulatin
    for spine in ['top','right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

if __name__ == '__main__':
    main()
    plt.show()
