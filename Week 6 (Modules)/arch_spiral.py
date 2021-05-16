###############################################################################
# Author: Karteikay Dhuper
# Date: March 22nd 2021
# Description This program draws an Archimedian spiral using turtle graphics.
###############################################################################

from turtle import * # imports everything from the turtle graphics module
from math import * # imports everything from the math module

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    speed(10)
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    speed(10) # increases turtle speed so trial and error testing can be sped up

    for i in range(241): # for loop iterates through range of values that feed theta
        theta = i / 20 * pi # theta is calculated in radians
        # equation from instructions implimented to find x,y values on cartesian plane
        x = (degrees(theta) / 10) * cos(theta)
        # degrees is used to convert theta value from raidans to degrees
        y = (degrees(theta) / 10) * sin(theta)
        goto(x,y)
    up()

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
