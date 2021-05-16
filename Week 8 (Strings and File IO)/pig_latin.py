################################################################################
# Author: Karteikay Dhuper
# Date: April 4th 2021
# Description This program converts a user provided phrase into pig latin.
################################################################################

def pig(string):

    oldString = string.lower() #input argument is referred to as oldString and everything is lowercased
    wordList = oldString.split() # input argument is split up by words in list
    newString = []
    for word in wordList: # for loop iterates through words in string list
        newWord = word[1:] + word[0] + "ay" + "" #converts word to pig latin
        newString.append(newWord) # adds iterated words to new list
    newString[0] = newString[0].capitalize() # capitalizes first word
    finalString = ' '.join(newString) # prints each element of list seperately
    return finalString

def main():

    string = input("Enter a string: ")# input statement
    print(pig(string))


if __name__ == '__main__':
    main()
