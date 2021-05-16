################################################################################
# Author: Karteikay Dhuper
# Date: March 12th 2021
# Description This program guides a turtle out of a maze
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    forward(11)
    right(90)
    forward(85)
    left(90)
    forward(50)
    right(90)
    forward(20)
    left(90)
    forward(20)
    right(90)
    forward(100)
    left(90)
    forward(50)
    right(90)
    forward(20)
    left(90)
    forward(70)
    left(90)
    forward(45)
    right(90)
    forward(25)
    left(90)
    forward(180)
    right(90)
    forward(15)


# Don't change this
if __name__ == '__main__':
    main()
    done()
