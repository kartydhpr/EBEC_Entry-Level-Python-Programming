###############################################################################
# Author: Karteikay Dhuper
# Date: March 22nd 2021
# Description This program draws the vowels "a e i o u" in a random order
# determined in runtime using the vowels.py module written by me
###############################################################################

from turtle import *

# Add your imports here -------------------------------------------------------
import vowels as v # import vowel.py
import random as r # import random module from python 

def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(1)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------

    # creates an array list with instructions to draw a letter in each index
    vowels = [v.draw_a,v.draw_e,v.draw_i,v.draw_o,v.draw_u]
    # calls the shuffle function from the random module to shuffle array list
    r.shuffle(vowels)
    # for loop iterates through array list (after its been shuffled)
    # and returns each index as a function call
    for i in vowels:
        i()

    #r.shuffle(vowels)
    print(vowels)



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
