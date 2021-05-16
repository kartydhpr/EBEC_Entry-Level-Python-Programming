################################################################################
# Author: Karteikay Dhuper
# Date: April 23rd 2021
# Description This program displays the result of rolling a side with n side
# n number of times
################################################################################

import random as r

class Dice:

    def __init__ (self, sides): #constructor method --> initializes variables
        self.sides = sides

    def roll(self):
        diceRoll = r.randint(1,self.sides) # dice randomly returns value between 1 and number od sides in instance of dice object (inclusive of 1 and 6)

        return diceRoll

    def n_rolls(self, numRolls):
        rollList = []
        print(f"Rolling a {self.sides} sided die {numRolls} times:", end = ' ')
        for i in range(numRolls - 1): # calls the roll() method 'numRolls' number of times
            print(str((self.roll())) + ',', end = ' ') # appends it to the list
            if i == numRolls -2:
                print((self.roll()))

        return None

def main():

    sixSides = Dice(6) # creates dice object with 6 sides
    tenSides = Dice(10) # creates dice object with 10 sides
    twentySides = Dice(20) # creates dice object with 20 sides

    sixRollResult = sixSides.n_rolls(10)
    tenRollResult = tenSides.n_rolls(10)
    twentyRollResult = twentySides.n_rolls(10)


if __name__ == '__main__':
    main()
