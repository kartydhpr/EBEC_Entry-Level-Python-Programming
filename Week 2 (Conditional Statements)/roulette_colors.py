################################################################################
# Author: Karteikay Dhuper
# Date: 2/12/2021
# This program displays whether a pocket number is red, green or black
# based on the pocket number inputted
################################################################################

#asks user to input pocket number
pocket = int(input("Please enter a pocket number: "))

#conditional statement that checks if inputted pocket is green
if (pocket == 0):
    print("  "+"Pocket 0 is green.")

#conditional statement that checks if inputted pocket b/w 1-10 is either black
#or red based on whether or not it's even or odd
elif (1 <= pocket <= 10 ):
    # mod 2 = 0 checks if its even or not
    if (pocket % 2 == 0):
        print("  "+f"Pocket {pocket} is black.")
    #if even statement is not satisifed that means pocket is odd so else is called
    else:
        print("  "+f"Pocket {pocket} is red.")

# same logic as above elif statement except this checks pockets between 11-18
elif (11 <= pocket <= 18):
    if (pocket % 2 == 0):
        print("  "+f"Pocket {pocket} is red.")
    else:
        print("  "+f"Pocket {pocket} is black.")

# same logic as above elif statement except this checks pockets between 19-28
elif (19 <= pocket <= 28):
    if (pocket % 2 == 0):
        print("  "+f"Pocket {pocket} is black.")
    else:
        print("  "+f"Pocket {pocket} is red.")


# same logic as above elif statement except this checks pockets between 29-36
elif (29 <= pocket <= 36):
    if (pocket % 2 == 0):
        print("  "+f"Pocket {pocket} is red.")
    else:
        print("  "+f"Pocket {pocket} is black.")

#statement prints if input doesn't satisfy any of the elif or if statements
else:
    print("  "+"Invalid Input!")
