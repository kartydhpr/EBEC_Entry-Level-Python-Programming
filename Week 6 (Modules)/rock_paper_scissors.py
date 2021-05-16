###############################################################################
# Author: Karteikay Dhuper
# Date: March 21st 2021
# Description This program lets the user play rock, paper, scissors against
# the computer.
###############################################################################
import random as fluxCapicator #<-- is alias for random -- thought it sounded cool

loseMessage = "  You lost.  Better luck next time."
winMessage = "  You won the game!"

def get_computer_choice():
    moves = ["rock","paper","scissors"] # array stores all the choices available
    computerChoice = fluxCapicator.choice(moves) #.choice chooses randomly from list
    return computerChoice

def get_player_choice():
    moves = ["rock","paper","scissors"]
    userChoice = input("Choose rock, paper, or scissors: ")

    while userChoice not in moves:
        print("You made an invalid choice. Please try again.")
        userChoice = input("Choose rock, paper, or scissors: ")
    else:
        return userChoice

def get_winner(computerChoice, userChoice):
    winner = "default"

    # condition for when it is a tie and game needs to be restarted
    while (userChoice == computerChoice):
        winner = "tie"
        return winner

    # conditins that assess the winner of the game
    if (userChoice == "rock" and computerChoice == "paper"):
        winner = "computer"
        return winner
    elif (userChoice == "rock" and computerChoice == "scissors"):
        winner = "player"
        return winner
    elif (userChoice == "paper" and computerChoice == "scissors"):
        winner = "computer"
        return winner
    elif (userChoice == "paper" and computerChoice == "rock"):
        winner = "player"
        return winner
    elif (userChoice == "scissors" and computerChoice == "rock"):
        winner = "computer"
        return winner
    elif (userChoice == "scissors" and computerChoice == "paper"):
        winner = "player"
        return winner

def main():
    # Write your mainline logic here ------------------------------------------
    userChoice = get_player_choice() # stores user's move
    computerChoice = get_computer_choice() # stores computer's move

    # condition for when it is a tie and game needs to be restarted
    while (get_winner(computerChoice, userChoice) == "tie"):
        print(f"  The computer chose {computerChoice}, "+f"and you chose {userChoice}.")
        print("  Its a tie. Starting over.\n")
        userChoice = get_player_choice()

    # conditins that assess the winner of the game
    if (get_winner(computerChoice, userChoice) == "player"):
        print(f"  The computer chose {computerChoice}, "+f"and you chose {userChoice}.")
        print(f"  {userChoice} beats "+f"{computerChoice}")
        print(winMessage)
    elif (get_winner(computerChoice, userChoice) == "computer"):
        print(f"  The computer chose {computerChoice}, "+f"and you chose {userChoice}.")
        print(f"  {computerChoice} beats "+f"{userChoice}")
        print(loseMessage)

    # closing remark
    print("Thanks for playing.")

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
