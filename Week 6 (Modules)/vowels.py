###############################################################################
# Author: Karteikay Dhuper
# Date: March 22nd 2021
# Description This program draws the vowels "a e i o u" using python's turtle
# graphics module
###############################################################################

from turtle import *

width(9)

def draw_a(): # draws lowercase "a"
    setheading(0)
    forward(50)
    pendown()
    circle(40)
    circle(40,90)
    forward(40)
    left(180)
    forward(80)
    penup()
    left(90)
    forward(20)

def draw_e(): # draws lowercase "e"
    setheading(90)
    forward(40)
    pendown()
    setheading(0)
    forward(70)
    left(90)
    circle(40,180)
    circle(40,140)
    penup()
    setheading(0)
    forward(3)
    right(90)
    forward(14)
    setheading(0)
    forward(10)

def draw_i(): # draws lowercase "i"
    forward(30)
    pendown()
    setheading(90)
    forward(80)
    penup()
    setheading(270)
    forward(80)
    left(90)
    forward(30)

def draw_o(): # draws lowercase "o"
    setheading(0)
    forward(50)
    pendown()
    circle(40)
    penup()
    forward(55)

def draw_u(): # draws lowercase "u"
    setheading(90)
    forward(40)
    pendown()
    setheading(90)
    forward(40)
    setheading(270)
    forward(45)
    circle(35,180)
    forward(45)
    left(180)
    forward(80)
    penup()
    setheading(0)
    forward(30)



def main():

    # You can use this for your own testing.
    draw_a()
    draw_e()
    draw_i()
    draw_o()
    draw_u()

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
