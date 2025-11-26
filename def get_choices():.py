import random

def get_choices():
    player_choice = input("Enter a choice (Rock,Paper,Scissor): ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")

    if player == computer:
        return "it's a tie!" 
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smasher the Scissors! You Win!"
        else:
            return "Paper covers Rock! You Lost!"  
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers Rock! You Win!"
        else:
            return "Scissors cuts Paper! You Lost!"   
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper! You Win!"
        else:
            return "Rock smasher the Scissors! You Lost!"
    else:
        return "Invalid Input! Please choose Rock, Paper, or Scissors."
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

