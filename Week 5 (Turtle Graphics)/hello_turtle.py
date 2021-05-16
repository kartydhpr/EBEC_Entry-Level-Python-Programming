################################################################################
# Author:
# Date:
# Description ...
################################################################################

# Don't change this
from turtle import *

def draw_e():
    # Write this function
    pendown()
    setheading(0)
    forward(45)
    left(90)
    circle(12,180)
    circle(12,160)


def draw_h():
    # Write this function
    speed(5)
    pendown()
    setheading(270)
    forward(60)
    right(180)
    forward(15)
    circle(-10,180)
    forward(15)
    penup()

def draw_l():
    # Write this function

    pendown()
    setheading(270)
    forward(60)
    penup()

def draw_o():
    # Write this function
    pendown()
    circle(12)

def draw_r():
    # Write this function
    heading()
def draw_t():
    # Write this function
    heading()
def draw_u():
    # Write this function
    heading()
def main():
    draw_h()
    goto(10,0)
    draw_e()
    draw_l()
    draw_l()
    draw_o()

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here

# Don't change this
if __name__ == '__main__':
    main()
    done()
