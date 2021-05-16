################################################################################
# Author: Karteikay Dhuper
# Date: March 7th 2021
# Description: Determines average grades for a list of 5 given by user
################################################################################

# Write function(s) here
def get_valid_score(): # method returns value of valid scores from user input
    score = float(input("Enter a score: "))
    # while loop prints error message while score is above 100 || below 0
    while ( score < 0 or score > 100):
        print("Invalid Input. Please try again.")
        # as long as input is invalid program will keep asking for input
        score = float(input("Enter a score: "))


    else:
        return score

def calc_average(gradeList): # method that calcs. average
    # adds all indexes in array divided by length of the array
    average = sum(gradeList)/len(gradeList)
    return average

def determine_grade(score): # method that maps value of score to letter grade
    if(90<=score<=100):
        return "A"
    elif(80<=score<=90):
        return "B"
    elif(70<=score<=80):
        return "C"
    elif(60<=score<=70):
        return "D"
    else:
        return "F"

def main():
    # Write your 'mainline logic' here
    gradeList = []
    # for loop iterates through 5 passes of getting and determining grade method
    for passThrough in range (1,5):
        # while loop keeps running methods to obtain 5 scores and letter grades
        while(passThrough < 6):
            score = get_valid_score() # stores return value from method call
            print(f"The letter grade for {score}"+f" is {determine_grade(score)}.")
            gradeList += [score] # adds new index with current iteration's score
            passThrough+=1
        else:
            # after 5 scores collected, average is printed using method
            print(f"The average score is {calc_average(gradeList):.2f}.")
            break

if __name__ == '__main__':
    main()
