###############################################################################
# Author: Karteikay Dhuper
# Date: March 21st 2021
# Description This program generates a simple math quiz with two random numbers
# one of which is 2 digits and the other is 3 digits.
###############################################################################

import random as r

# method declaration
def random_number(digits): # digits argument specifies number of digits
    if(digits == 2):
        integer = r.randrange(10,100)
    elif (digits == 3):
        integer = r.randrange(100,1000)
    return integer

def main():
    # Write your mainline logic here ------------------------------------------

    #variable declaration
    firstInt = random_number(2)
    secondInt = random_number(3)

    # prints the question
    print(f"   {firstInt}")
    print(f"+ {secondInt}")
    print(f"-----")
    # stores user's answer
    answer = int(input("= "))

    #checks if the answer was correct
    if (answer == firstInt + secondInt):
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {firstInt+secondInt}.")

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
