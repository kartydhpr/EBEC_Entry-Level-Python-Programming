################################################################################
# Author: Karteikay Dhuper
# Date: March 7th 2021
# Description: This program lists all the prime numbers from 2
# to a user specified limit
################################################################################

# Write function(s) here
def is_prime(number):
    # variable instantiation
    isPrime = True
    # prime determining logic
    if (number > 1):
        for i in range(2, int(number**0.5)+1): # iterates from 2 to sqrt(number)
            if number % i == 0: # if num can be / by any number b/w 2 and sqrt(num)
                isPrime = False # its not prime
                break
            else:
                isPrime = True
    else:
        isPrime = False # 1 is not a prime number
    return isPrime  # return statment
def main():
    # Write your 'mainline logic' here
    number = int(input("Enter a positive integer: "))
    primeList = []
    # for loop iterates through 2 and user specified limit
    for passThrough in range(2,number+1):
        # if statement adds number to array as new index if number is prime
        if is_prime(passThrough) == True:
            primeList += [passThrough]
            passThrough += 1
        else:
            passThrough += 1
    # print statements
    print(f"The primes up to {number} are: ", end = '')
    print(*primeList, sep = ', ')

if __name__ == '__main__':
    main()
