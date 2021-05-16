################################################################################
# Author: Karteikay Dhuper
# Date: 02/11/2021
# This program displays the number of days in February
# in the year that the user inputs
################################################################################

# this line declares the year variable and asks the user to fill it with a year
year = int(input("Please input a year: "))

# first if statement that checks if the year is divisble by 100 and also by 400
# then prints 29 days in Feb if satisfied
if (year % 100 == 0 and year % 400 == 0):
    print (f"In the year {year}, there are 29 days in February.")

# if year is not divisible by 100 AND 400 then go straight to checking if it is divisible by 4
# only if it is also not divisible by 100. If satisfied print 29 days in Feb.
elif (year % 100 != 0 and year % 4 == 0):
    print (f"In the year {year}, there are 29 days in February.")
    
# if none of the leap year conditions are met then program prints that there are only 28 days in february for chosen year
else:
    print(f"In the year {year}, there are 28 days in February.")
