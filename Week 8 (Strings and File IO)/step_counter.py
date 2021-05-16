################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program displays the average number of steps taken per month
# using data from a seperate file with steps for each day of the year
################################################################################
#from numpy import mean

def main():

    allSteps = [] # stores values for daily steps from file

    with open('steps.txt') as fo: # context manager created
        for lines in fo:
            allSteps.append(int(lines.rstrip())) # appends each value of step to list as int

    # month list stores name of each month
    monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    print("The average steps taken each month were:")
    for month in monthList: # first for loop iterates through and prints each month in monthlist
        print(f"{month.rjust(10)} "+":", end = ' ') # each month is right justified with width 10 padding
        for step in month: # nested for loop should print average of each month
            if(month=="January"):
                print(f"{sum(allSteps[0:31])/len(allSteps[0:31]):.1f}") # uses sum() / len() functions to calculate mean for sliced portion of allSteps list
            elif(month == "February"):
                print(f"{sum(allSteps[31:59])/len(allSteps[31:59]):.1f}")
            elif(month == "March"):
                print(f"{sum(allSteps[59:90])/len(allSteps[59:90]):.1f}")
            elif(month == "April"):
                print(f"{sum(allSteps[90:120])/len(allSteps[90:120]):.1f}")
            elif(month == "May"):
                print(f"{sum(allSteps[120:151])/len(allSteps[120:151]):.1f}")
            elif(month == "June"):
                print(f"{sum(allSteps[151:181])/len(allSteps[151:181]):.1f}")
            elif(month == "July"):
                print(f"{sum(allSteps[181:212])/len(allSteps[181:212]):.1f}")
            elif(month == "August"):
                print(f"{sum(allSteps[212:243])/len(allSteps[212:243]):.1f}")
            elif(month == "September"):
                print(f"{sum(allSteps[243:273])/len(allSteps[243:273]):.1f}")
            elif(month == "October"):
                print(f"{sum(allSteps[273:304])/len(allSteps[273:304]):.1f}")
            elif(month == "November"):
                print(f"{sum(allSteps[304:334])/len(allSteps[304:334]):.1f}")
            elif(month == "December"):
                print(f"{sum(allSteps[334:366])/len(allSteps[334:366]):.1f}")
            break

if __name__ == '__main__':
    main()
