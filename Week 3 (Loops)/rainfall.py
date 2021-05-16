################################################################################
# Author: Karteikay Dhuper
# Date: 2/20/2021
# This program calculates average rainfall over a period of years
# based on data for each month input by user
################################################################################

# initialization of required variables
numYears = int(input("Enter the number of years: "))
monthCounter = 0
total = 0

# arrayList of calendar months so that indexes can be called for a particular month
monthList = ["Jan.","Feb.","Mar.","Apr.","May.","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec."]

# if-statement that checks if inputted years is valid then runs nested for loop
if numYears > 0 :

    for i in range(numYears):
        print("  "+f"For year No. {i+1}")

        for j in range(len(monthList)):
            rainfall = float(input("    "+f"Enter the rainfall for {monthList[j]}: "))

            # while-loop keeps firing until user puts positive value
            while rainfall < 0:
                print("    "+"Invalid input, please try again.")
                rainfall = float(input("    "+f"Enter the rainfall for {monthList[j]}: "))

            monthCounter += 1
            total += rainfall

    # print statments that fire after nested for loop has been fully iterated succesfully
    print(f"There are {monthCounter} months.")
    print(f"The total rainfall is {total:.2f} inches.")
    print(f"The monthly average rainfall is {total/monthCounter:.2f} inches.")

# if inputted years doesn't pass validity test then print statment is printed
else:
    print("Invalid input.")
