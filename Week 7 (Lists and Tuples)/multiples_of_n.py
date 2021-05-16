################################################################################
# Author: Karteikay Dhuper
# Date: March 28th 2021
# Description This program returns a list of integers from the second argument
# that are multiples of its first argument.
################################################################################

def multiples_of(n, number_list):
    new_list = [] # new modified list to return
    for i in number_list: # for loop iterates contents of list
        if(i%n == 0): # mod checks if i is evenly divisible by n
            new_list.append(i) # i is then added to the new list
        i += 1 # next iteration
    return new_list


def main():

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]
    print("Original list of numbers:")
    print(number_list)
    print(f"Numbers in the list that are multiples of 7:")
    print(multiples_of(7,number_list))

if __name__ == '__main__':
    main()
