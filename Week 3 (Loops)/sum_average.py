################################################################################
# Author: Karteikay Dhuper
# Date: 2/20/2021
# This program generates the sum and average
# based on numbers inputted by user
################################################################################

# counter counts the number of iterations
count = 0
# total stores accumulated value of all numbers
total = 0
# msg stores string variable for message
msg = "Enter a non-negative number (negative to quit): "
# number stores current iterations inputted number as a float/double
number = float(input(msg))

# while loop asks for number input as long as the inputted number is not -ve
while (number >= 0):
    # counter is incremented while statement is true
    count += 1
    # accumulator adds the current number to total
    total += number
    # input message is printed and stores input as a float number
    number = float(input(msg))

# if-statement checks if the first input is negative
if(number < 0 and count == 0):
    print("No input.")
# if not negative then proceed to print the sum and average
else:
    print(f"Sum = {total:.2f}")
    print(f"Average = {total/count:.2f}")
