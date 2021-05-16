################################################################################
# Author: Karteikay Dhuper
# Date: March 28th 2021
# Description This program collects 10 floating point numbers and
################################################################################

def get_number_list(): # method asks user for 10 floating point numbers
    countup = 1
    number_list = []
    while (countup < 11): # while loop only exits after 10 numbers have been entered
        inputNumber = float(input(f"  Enter number {countup:2d} of 10: "))
        number_list.append(inputNumber) # adds to end of list
        countup += 1  # increment
    return number_list


def main():

    generated_list = get_number_list() # stores method generated list
    lowest = min(generated_list) # stores smallest number
    highest = max(generated_list) # stores largest number
    print(f"Lowest number: {lowest:.2f}")
    print(f"Highest number: {highest:.2f}")

    total = 0
    for i in generated_list: # for loop accumulates total from list
        total += i
        i += 1
    print(f"Total: {total:.2f}")
    average = total / 10
    print(f"Average: {(average):.2f}")

if __name__ == '__main__':
    main()
