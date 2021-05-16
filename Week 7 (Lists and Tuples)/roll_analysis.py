################################################################################
# Author: Karteikay Dhuper
# Date: March 28th 2021
# Description This program calculates and prints the percentage of rolls that
# total each value between 2 and 12 when two dices are rolled randomly.
################################################################################

import random as r

def roll_d6(): # function rolls one dice
    diceRoll = r.randint(1,6) # dice randomly returns value between 1-6 (inclusive of 1 and 6)
    return diceRoll

def get_2d6_rolls(simulations): # returns sum of two dice rolls
    s = simulations
    rollHistory = [] # list stores history of two roll sums
    # adds 900 000 two roll sums to the list
    for i in range(s): # rolls two dices 900 000 times
        rollOne = roll_d6() # rolls one dice
        rollTwo = roll_d6() # rolls another dice
        twoRolls = rollOne + rollTwo  # computes sum of both dice rolls
        rollHistory.append(twoRolls) # adds sum of two to a list -- does this 900 000 times
        i += 1  # iterates
    return rollHistory

def main():
    simulations = 900000 # this is the number of times to roll the dice
    rollHistoryOutput = get_2d6_rolls(simulations) # stores array list
    #print(rollHistoryOutput)

    print("Roll  Frequency")
    for i in range (2,13): # prints frequency for each sum value
        occurances = rollHistoryOutput.count(i) # counts number of occurances for each sum value
        frequency = (occurances / simulations)*100 # frequency calculation

        # print formatting
        print(f" {i:2d}", end = '')
        print(f"    {frequency:5.2f}%")
        i+=1 # iteration

if __name__ == '__main__':
    main()
