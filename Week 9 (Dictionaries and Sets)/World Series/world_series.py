################################################################################
# Author: Karteikay Dhuper
# Date: April 11th 2021
# Description This program returns the winner of the word series on the year that
# the user asks it to. The winners are stored in a dictionary.
################################################################################

def load_winners_data(): # this function returns two dictionaries

    dictionary1 = {}
    dictionary2 = {}

    with open("WorldSeriesWinners.txt") as fo: # context manager created
        lines = list(fo.readlines()) # puts all the lines from input file in list

        year = 1902 # started year that gets 1 added to it in for loop
        for line in lines: # for loop adds a year to each team name
            if year == 1993 or year == 1903:
                year += 1 #skips 1994 and 1904
            year += 1 # adds 1 to year
            key = (year) # so that key increases yearly
            value = line[:-1] # value for each year key is line from file with "\n" removed
            dictionary2[key] = value

        for line in lines: # for loop that generates dictionary with winners and number of times they've won
            string = line
            value = string[:-1]
            if value in dictionary1.keys(): # if team name is in the keys
                dictionary1[value] += 1 # then add one to the team key's value to store how many victories they accumulated
            else:
                dictionary1[value] = 1 #otherwise if its the first time encountering team store victory as first victory in values

        return dictionary1, dictionary2


def main():
        dictionaryList = load_winners_data()


        year = int(input("Enter a year in the range 1903 -- 2020: "))
        if int(year) > 2020 or int(year) < 1903:
            print(f"Data for the year {year} is not included in this system.")
        elif int(year) == 1904 or int(year) == 1994:
            print(f"The World Series wasn't played in the year {year}.")
        else:
            print(f"The {dictionaryList[1][year]} won the World Series in"+f" {year}.")
            print(f"They have won the World Series {dictionaryList[0][dictionaryList[1][year]]} times.")

if __name__ == '__main__':
    main()
