################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program displays file statistics for the file created from the
# last excercise
################################################################################

def main():

    lines = [] # creares array that stores numbers as lines

    with open("random_numbers.txt") as fo: # context manager created
        for line in fo: # for loop adds each line to list
            lines.append(int(line.rstrip()))

    # print statements
    print(f"{len(lines):,} numbers were read from the file.")
    print(f"Max: {max(lines)}")
    print(f"Min: {min(lines)}")

    total = 0 # accumulator
    for i in lines: # for loop to sum contents of list
        total += i
        i += 1
    sum = total

    print(f"Sum: {sum:,}")
    print(f"Avg: {sum/len(lines):.1f}")


if __name__ == '__main__':
    main()
