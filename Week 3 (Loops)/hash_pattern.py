################################################################################
# Author: Karteikay Dhuper
# Date: 2/20/2021
# This program draws a hash pattern
# based on number of lines inputted by user
################################################################################

# intitlaizes variable that stores number of lines to be printed
numLines = int(input("Enter the number of lines: "))

# for loop iterates over number of lines and stores whitespace value
for r in range(numLines):
    whitespaces = ""
    # nested for loop that increments number of white spaces per first for loop
    for c in range(r): 
        whitespaces += " "
    print("#" +f"{whitespaces}" + "#")
