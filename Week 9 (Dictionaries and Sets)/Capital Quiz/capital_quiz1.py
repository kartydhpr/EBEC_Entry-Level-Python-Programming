################################################################################
# Author: Karteikay Dhuper
# Date: April 11th 2021
# Description This program quizzes the user by asking them to enter the capital
# of a particular state until all states have been answered.
################################################################################
import random as r

def get_state_data(): # this function gets

    # intiialize empty dictionary for state and capital pairings
    stateCapitals_Dictionary = {}

    with open('state_capitals.txt') as fo: # opens file with state capitals through context manager
        for i in fo:
            QandA = i.split(",") # splits each line by the "," and saves it as index in a list
            oldKey = QandA[1] # specifies that key is state name
            key = oldKey[:-1].lstrip() # removes "\n" from state name and also removes leading whitespace
            value = QandA[0] # specifies that value for key is the capital city
            stateCapitals_Dictionary[key] = value # maps value to key
            # this is done for every line in input file -- as it is in a for loop

    return stateCapitals_Dictionary

def main():
    # counts number of iterations
    count = 0
    # stores total correct counts
    totalCorrect = 0

    for state,capital in get_state_data().items():

        userAnswer0 = input(f"What is the capital of {state} (enter 0 to quit)? ")
        userAnswer = userAnswer0.title()

        if userAnswer == '0': # if user enter 0 then the for loop breaks and it goes to the score print statment
            break

        elif(userAnswer == capital):
            print("That is correct!")
            totalCorrect+=1
            count+=1

        else:
            print("That is incorrect.")
            print(f"The capital of {state}"+f" is {capital}.")
            count+=1

    print(f"You answered {totalCorrect}"+f" out of {count} questions correctly.")

if __name__ == '__main__':
    main()
