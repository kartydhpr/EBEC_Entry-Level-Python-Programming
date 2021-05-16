################################################################################
# Author: Karteikay Dhuper
# Date: April 18th 2021
# Description This program will generate a plot of the total positive cases
# of Covid-19 in Indiana.
################################################################################
import matplotlib.pyplot as plt

def main():

    dates = []

    with open("2008_Weekly_Gas_Averages.txt") as fo:
        for line in fo:
            dates = line.rstrip('')

    print(dates)    
    # x = []
    # for date in dates:
    #     y, m, d = date.split('-')
    #     dt = datetime.date(int(y),int(m),int(d))
    #     x.append(dt)




if __name__ == '__main__':
    main()
    plt.show()
