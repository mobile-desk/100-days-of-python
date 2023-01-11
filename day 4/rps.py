from random import *

list = ["rock", "paper", "scissors"]

user = input("Enter here: ").lower().strip()
computer = choice(list)
print(f"The computer played {computer}")

if user in list:
    if user == "rock":
        if computer == "rock":
            print(f"It was a tie")
        elif computer == "paper":
            print(f"You lose")
        else:
            print(f"You won")

    elif user == "paper":
        if computer == "rock":
            print(f"You won")
        elif computer == "paper":
            print(f"It was a tie")
        else:
            print(f"You lost")

    else:
        if computer == "rock":
            print(f"You lost")
        elif computer == "paper":
            print(f"you won")
        else:
            print(f"it was a tie")
else:
    print("invalid play")

