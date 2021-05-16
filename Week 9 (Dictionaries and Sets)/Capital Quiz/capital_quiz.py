################################################################################
# Author: Karteikay Dhuper
# Date: April 11th 2021
# Description This program quizzes the user by asking them to enter the capital
# of a particular state until all states have been answered.
################################################################################

def get_state_data(): # this function gets the state and capital pairs from an input file and adds them to a dictionary

    # intiialize empty dictionary for state and capital pairings
    stateCapitals_Dictionary = {}

    with open('state_capitals.txt') as fo: # opens file with state capitals through context manager
        for list in fo:
            QandA = list.split(",") # splits each line by the "," and saves it as index in a list
            oldKey = QandA[1] # specifies that key is state name
            key = oldKey[:-1].lstrip() # removes "\n" from state name and also removes leading whitespace
            value = QandA[0] # specifies that value for key is the capital city
            stateCapitals_Dictionary[key] = value # maps value to key
            # this is done for every line in input file -- as it is in a for loop

    return stateCapitals_Dictionary

def main():

    count = 0     # counts number of iterations
    totalCorrect = 0     # stores total correct counts
    questionList = get_state_data().items()
    exit = False; # boolean stores whether or not program should exit

    while questionList:
        incorrectList = []  #Temporarily holds the incorrect elements

        if exit == True:
            break
        for state,capital in questionList:
            userAnswer0 = input(f"What is the capital of {state} (enter 0 to quit)? ")
            userAnswer = userAnswer0.title()

            if userAnswer == '0': # if user enter 0 then the for loop breaks and it goes to the score print statment
                exit = True
                break

            elif(userAnswer == capital):
                print("That is correct!")
                totalCorrect+=1 # adds to the total correct answer accumulator variable
                count+=1   # adds to total number of questions asked

            else:
                print("That is incorrect.")
                print(f"The capital of {state}"+f" is {capital}.")
                count+=1
                quizAgain = (state,capital)
                incorrectList.append(quizAgain) #adds temp item to the end of list
        questionList = incorrectList
    print(f"You answered {totalCorrect}"+f" out of {count} questions correctly.")

if __name__ == '__main__':
    main()
