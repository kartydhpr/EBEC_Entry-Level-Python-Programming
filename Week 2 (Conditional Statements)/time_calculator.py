################################################################################
# Author: Karteikay Dhuper
# Date: 2/12/2021
# This program converts seconds inputted by a user into a more readable format
################################################################################

# stores input of seconds given by user
seconds = int(input("Please enter a time in seconds. "))

# converts seconds into number of seconds left over
timeInSeconds = seconds % 60
# converts seconds into minutes
timeInMinutes = seconds % 3600 //60
# converts seconds into hours
timeInHours = seconds % 86400 // 3600
# converts seconds into days
timeInDays = seconds//86400

# string variables that are used to concatonate based on conditional scenarios
stringOpening = ("  "+ f"{seconds:,} seconds is:")
stringDays = (f"{timeInDays} day(s)")
stringHours = (f"{timeInHours} hour(s)")
stringMinutes = (f"{timeInMinutes} minute(s)")
stringSeconds = (f"{timeInSeconds} second(s)")


# conditional statement that checks if seconds is less than 60 then prints message
if (seconds < 60):
	print("  "+"The number of seconds is less than one minute.")

# conditional statment that fires if prior is not met
# prints conversion from seconds to minutes as the highest order of magnitude
elif (3600 > seconds >= 60):
	print(stringOpening + " " + stringMinutes, end = "")
	if(timeInSeconds != 0):
		print(" and "+stringSeconds, end = "")
	print(".")

# conditional statement that fires if prior is not met
# prints conversion from seconds to hours as the highest order of magnitude
elif (86400 > seconds >= 3600):
	print(stringOpening + " "+ stringHours, end = "")

	if(timeInMinutes and timeInSeconds != 0):
		print(",", end = '')
	elif(timeInMinutes ^ timeInSeconds !=0):
		print(" and", end = '')

	if (timeInMinutes != 0 and timeInSeconds == 0):
		print(" "+stringMinutes, end = "")
	elif (timeInMinutes and timeInSeconds !=0):
		print(" "+stringMinutes+" and" , end = "")

	if (timeInSeconds != 0):
		print(" "+stringSeconds, end = "")

	print(".")

# conditional statement that fires if prior is not met
# prints conversion from seconds to days as the highest order of magnitude
elif (seconds >= 86400):
	print(stringOpening + " " + stringDays, end = "")

	if(timeInHours != 0):
		print(", "+stringHours, end = "")

	if(timeInMinutes and timeInSeconds != 0):
		print(",", end = '')
	elif(timeInMinutes ^ timeInSeconds !=0):
		print(" and", end = '')

	if (timeInMinutes != 0 and timeInSeconds == 0):
		print(" "+stringMinutes, end = "")
	elif (timeInMinutes and timeInSeconds !=0):
		print(" "+stringMinutes+" and" , end = "")

	if (timeInSeconds != 0):
		print(" "+stringSeconds, end = "")

	print(".")
