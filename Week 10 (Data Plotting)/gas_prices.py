################################################################################
# Author: Karteikay Dhuper
# Date: April 18th 2021
# Description This program generates a graph using matplotlib to plot the weekly
# gas prices in 2008
################################################################################
import matplotlib.pyplot as plt

def main():

    #variable initialization
    gasAverage = [] # stores gas averages from input file

    # context manager created for file i/o
    with open("2008_Weekly_Gas_Averages.txt") as fo:
        for line in fo:
            gasAverage.append(float(line.rstrip())) # adds each line from file at the end of the "gasAverage" list

    # plotting specifications
    fig, ax = plt.subplots()   # initialize plot
    ax.set_title("2008 Weekly Gas Prices") # set title
    ax.set_xlabel("Weeks (by number)") #labels x axis
    ax.set_ylabel("Average Price (dollars/gallon)") # labels y axis
    ax.set_xticks([10,20,30,40,50]) # specifies ticks for the x axis
    ax.set_xlim(1,52) # specifies limit for x-axis as 0-52
    ax.set_ylim(1.5,4.25) # specifies y-axis limit
    ax.grid() #adds grids to the figure
    ax.plot(gasAverage) # plots graph (stored in memory until "plt.show" is called)


if __name__ == '__main__':
    main()
    plt.show()
