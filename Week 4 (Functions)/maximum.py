################################################################################
# Author: Karteikay Dhuper
# Date: March 3rd 2021
# Description: This program returns the bigger number between two numbers
# provided by the user
################################################################################

# Write function(s) here
def max_of_two(int1, int2):
    # if statement that returns which is bigger
    if(int1>int2):
        return int1
    else:
        return int2

def main():
    # integer inputs
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    # variable stores function result
    result = max_of_two(int1, int2)
    #print statement
    print(f"{result} is greater.")

if __name__ == '__main__':
    main()
