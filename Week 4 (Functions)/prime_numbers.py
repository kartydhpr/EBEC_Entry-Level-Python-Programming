################################################################################
# Author: Karteikay Dhuper
# Date: March 7th 2021
# Description: Program returns whether number is prime or not.
################################################################################

# Write function(s) here
def is_prime(number):
    isPrime = True

    if (number > 1):
        for i in range(2, int(number**0.5)+1): # iterates from 2 to sqrt(number)
            if number % i == 0: # if num can be / by any number b/w 2 and sqrt(num)
                isPrime = False # its not prime
                break
            else:
                isPrime = True
    else:
        isPrime = False # 1 is not a prime number

    return isPrime

def main():
    # Write your 'mainline logic' here
    msg = "Enter a positive integer (-1 to quit): "
    number = int(input(msg))

    # while loop executes if else statement as long as number is not -1
    while (number != -1):
        if is_prime(number) == True: # calls method and prints statement
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
        number = int(input(msg))



if __name__ == '__main__':
    main()
