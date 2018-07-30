
import random

print("Welcome. You will be playing rock, paper, scissors against a computer. Don't worry; the computer (probably) won't cheat.")

combo = ('rock', 'paper', 'scissors')

win_count = 0
tie_count = 0
lose_count = 0

cont_ans = "y"

while cont_ans == "y":

    player_choice = input("Pick rock, paper, or scissors: ")
    
    player_choice = player_choice.lower()
    
    #Randomly picks rock, paper, or scissors.
    comp_choice = random.choice(combo)
    
    if player_choice == "rock" and comp_choice == "paper":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You lost.")
        lose_count = lose_count + 1
    elif player_choice == "rock" and comp_choice == "scissors":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You won!")
        win_count = win_count + 1
    elif player_choice == "paper" and comp_choice == "scissors":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You lost.")
        lose_count = lose_count + 1
    elif player_choice == "paper" and comp_choice == "rock":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You won!")
        win_count = win_count + 1
    elif player_choice == "scissors" and comp_choice == "rock":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You lost.")
        lose_count = lose_count + 1
    elif player_choice == "scissors" and comp_choice == "paper":
        print("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You won!")
        win_count = win_count + 1
    elif player_choice == comp_choice:
        ("You picked "+player_choice+".")
        print("The computer picked "+ comp_choice+".")
        print("You tied.")
        tie_count = tie_count + 1
    else:
        print("Please enter valid input.")
        continue
    
    cont_ans = input("Do you wish to continue? (y/n) ")
    
    if cont_ans == "y":
        continue
    elif cont_ans == "n":
        print("You won " + win_count + "time(s)")
        print("You tied " + tie_count + "time(s)")
        print("You lost " + lose_count + "time(s)")
        input()
        break
    else:
        print("Please enter valid input.")
        continue
    
input()
