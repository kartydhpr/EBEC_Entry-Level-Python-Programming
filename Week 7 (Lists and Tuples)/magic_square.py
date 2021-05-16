################################################################################
# Author: Karteikay Dhuper
# Date: March 28th 2021
# Description This program determines whether or not a square (formatted 2D list)
# is a Lo Shu magic square.
################################################################################

def print_square(square):
    s = square
    rows = 3
    cols = 3
     # nested for loop iterates through 2D array
    for r in range (rows):
        for c in range (cols):
            n = s[r][c] # each iteration stores 1 index from list inside list
            if( (r == 0 and c == 2) or (r == 1 and c == 2)  or (r == 2 and c == 2)):
                output = print(f"{n}", end = '')
            else:
                output = print(f"{n} ", end = '')
        print()
    return output

def is_magic(square):
    s = square

    isMagic = True # square set to true by default

    # condition for vertical addition
    if(s[0][0]+s[1][0]+s[2][0] and s[0][1]+s[1][1]+s[2][1]  and s[0][2]+s[1][2]+s[2][2] != 15):
        isMagic = False

    # condition for horizontal addition
    if(s[0][0]+s[0][1]+s[0][1] and s[1][0]+s[1][1]+s[1][2] and s[2][0]+s[2][1]+s[2][2] != 15):
        isMagic = False

    # condition for diagonal sum
    if(s[0][0]+s[1][1]+s[2][2] and s[0][2]+s[1][1]+s[2][0] != 15):
        isMagic = False

    # condition for number repitition
    flattenList = sum(s, []) # flatens original list by coverting 2d array to 1d array - for easier repitition check
    for i in range (1,9):
        occurances = flattenList.count(i) #checks for occurances of numbers 1-9
        if(occurances > 1): # if more than one occurance of any
            isMagic = False # then it is not magic square
        i+=1

    return isMagic

def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    # execution for first 2D array list:
    square = m1
    print("Your square is:")
    print_square(square)
    if (is_magic(square) == True):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
    print()

    # execution for second 2D array list:
    square = m2
    print("Your square is:")
    print_square(square)
    if (is_magic(square) == True):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
    print()


    # execution for third 2D array list:
    square = m3
    print("Your square is:")
    print_square(square)
    if (is_magic(square) == True):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
    print()

if __name__ == '__main__':
    main()
