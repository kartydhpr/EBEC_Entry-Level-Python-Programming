################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program reads the contents of a file and tracks the number
# of words and the number of lines in the file. It also calculates the average
# number of words per line.
################################################################################

def main():

    numLines = 0 # counter variable
    numWords = 0 # counter variable

    with open("rumpelstiltskin.txt") as fo:
        for line in fo: # for loop goes through each line in file object
            lines = line.strip() # lines are determined by stripping lines from main file
            words = line.split() # words determined by splitting whitespaces from lines
            numLines += 1 # number of lines increasews sequentially
            numWords += len(words) # number of words calculated using length of words list

    print(f"Total number of words: {numWords}")
    print(f"Total number of lines: {numLines}")
    print(f"Average number of words per line: {(numWords/numLines):.1f}")



if __name__ == '__main__':
    main()
