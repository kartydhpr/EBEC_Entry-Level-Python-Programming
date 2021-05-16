################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program converts a phone number with characters to a phone
# number with solely digits.
################################################################################

def convert_number(phoneNum):

    newString = phoneNum.upper() # converts entered phone number's characters to uppercase

    # converts letters to the digit "2"
    newString = newString.replace('A', '2')
    newString = newString.replace('B', '2')
    newString = newString.replace('C', '2')

    # converts letters to the digit "3"
    newString = newString.replace('D', '3')
    newString = newString.replace('E', '3')
    newString = newString.replace('F', '3')

    # converts letters to the digit "4"
    newString = newString.replace('G', '4')
    newString = newString.replace('H', '4')
    newString = newString.replace('I', '4')

    # converts letters to the digit "5"
    newString = newString.replace('J', '5')
    newString = newString.replace('K', '5')
    newString = newString.replace('L', '5')

    # converts letters to the digit "6"
    newString = newString.replace('M', '6')
    newString = newString.replace('N', '6')
    newString = newString.replace('O', '6')

    # converts letters to the digit "7"
    newString = newString.replace('P', '7')
    newString = newString.replace('Q', '7')
    newString = newString.replace('R', '7')
    newString = newString.replace('S', '7')

    # converts letters to the digit "8"
    newString = newString.replace('T', '8')
    newString = newString.replace('U', '8')
    newString = newString.replace('V', '8')

    # converts letters to the digit "9"
    newString = newString.replace('W', '9')
    newString = newString.replace('X', '9')
    newString = newString.replace('Y', '9')
    newString = newString.replace('Z', '9')

    return newString


def main():
    phoneNum = input("Enter a telephone number: ") # stores phone number
    print("The phone number is " f"{convert_number(phoneNum)}") # prints converted number from function

if __name__ == '__main__':
    main()
