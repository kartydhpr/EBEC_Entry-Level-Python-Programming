################################################################################
# Author: Karteikay Dhuper
# Date: March 8th 2021
# Description This program draws a hexagonal spiral
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    setheading(0)
    for i in range(5,200,5):
        forward(i)
        right(60)

# Don't change this
if __name__ == '__main__':
    main()
    done()
