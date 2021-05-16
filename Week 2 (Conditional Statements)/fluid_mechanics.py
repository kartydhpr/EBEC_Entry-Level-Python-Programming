################################################################################
# Author: Karteikay Dhuper
# Date: 2/18/2021
# This program calculates Reynolds number for Fluid Mechanics
# based on input values from user
################################################################################

# variables that store user input for calculating Reynolds Number
velocity = float(input("Enter the velocity of water in the pipe: "))
diameter = float(input("Enter the pipe's diameter: "))
temperature = float(input("Enter the temperature in °C as 5, 10, or 15: "))

# stores the value of kinematic kinematic viscosity after user inputs temperature
kinematicViscosity = 0

# computes value for kinematic viscosity based on user input
if(temperature == 5):
    kinematicViscosity = 1.49*10**-6
elif(temperature == 10):
    kinematicViscosity = 1.31*10**-6
elif(temperature == 15):
    kinematicViscosity = 1.15*10**-6
else:
    print("Invalid Temperature, please input either 5, 10 or 15 in °C ")

# stores computed value for Reynolds Number
reyNum = (velocity * diameter) / kinematicViscosity

# converts product of reyNum into scientific notation
sciNote = "{:.2e}".format(reyNum)

# prints finish statment
print("The Reynolds number for flow at "+ f"{velocity} m/s "+ f"in a {diameter} m diameter pipe at "+ f"{temperature}°C is "+ f"{sciNote}.")
