# import libraries
import random

def get_choices() -> dict:
    # a player has a choice
    # take input from the user as an input for the players
    player_choice = input("Enter a choice(rock, paper, scissors) : ")
    options = ["rock", "paper", "scissors"]
    # the computer has a choice but randomly from the options
    computer_choice = random.choice(options)
    choices = {"player": player_choice, 
               "computer": computer_choice}
    return choices

def check_win(player, computer) -> str:
    # concatenation is done by '+' sign
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It is a tie!"
    # Refactoring : using a nested if
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers scissors! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
    elif player == "paper":
        if computer == "rock":
            return "SPaper covers scissors! You win!"
        else:
            return "Scissors cut paper! You lose."
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


    
