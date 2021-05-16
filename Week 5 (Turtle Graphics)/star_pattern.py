################################################################################
# Author: Karteikay Dhuper
# Date: March 14th 2021
# Description This program draws a star pattern based on the number of points
# provided by the user
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    speed(10)
    bgcolor("black")
    pencolor("yellow")
    corners = int(input("How many points would you like the star to have? "))
    innerAngle = 360/corners
    concaveAngle = 2*innerAngle

    fillcolor("gold")

    begin_fill()

    right(90-(concaveAngle/2))
    for i in range(corners):
        forward(side_length)
        right(innerAngle-180)
        forward(side_length)
        left(concaveAngle-180)

    end_fill()

# Don't change this
if __name__ == '__main__':
    main()
    done()
