################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program randomly generates a user specified number of...well numbers
################################################################################
import random as r


def main():

    # asks for amount of random numbers to be generated in new file
    amountOfNums = int(input("Enter the number of random numbers to be written to the file: "))

    # creates a list for random numbers to be stored in
    numberList = []

    # for loop goes through and stores requested amount of random numbers in list
    for i in range(amountOfNums):
        number = r.randrange(1,501) # random numbers in range of 1-500
        # number appended to list with "\n" so they can be printed in a new line when written to file
        numberList.append(f"{number}\n")
        i+=1

    with open("random_numbers.txt", 'w') as fo: #context manager created
        fo.writelines(numberList) # number list is written to file

    

if __name__ == '__main__':
    main()
