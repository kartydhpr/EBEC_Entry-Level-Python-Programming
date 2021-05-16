################################################################################
# Author: Karteikay Dhuper
# Date: 2/22/2021
# This program predicts the approximate size of a population of organisms
# based on values inputted by the user
################################################################################

# variables that store user inputs
startNum = int(input("Starting number, in million: "))
incRate = float(input("Average daily increase, in percent: "))/100
multDays = int(input("Number of days to multiply: "))

#variable stores the population per iteration with start as default
population = startNum

# prints the header of the table
print("Day   Approx. Pop")

# for loop iterates over days and adds approproate population number
for i in range(1, multDays+1):
    print(f" {i:2d}","     ", f"{population:7.4f}")
    population = population + (incRate * population)
