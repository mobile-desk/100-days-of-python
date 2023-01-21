from random import *


def rps(user, computer):
    if user == computer:
        print("its a tie")
    elif (user == 'rock') and (computer == 'paper'):
        print("you lost")
    elif (user == 'rock') and (computer == 'scissors'):
        print("you won")
    elif (user == 'paper') and (computer == 'rock'):
        print("you won")
    elif (user == 'paper') and (computer == 'scissors'):
        print("you lost")
    elif (user == 'scissors') and (computer == 'paper'):
        print("you won")
    elif (user == 'scissors') and (computer == 'rock'):
        print("you lost")
    else:
        pass



list = ['rock', 'paper', 'scissors']

u = input("Please pick from the list ['rock', 'paper', 'scissors']: ").lower().strip()
c = choice(list)

print(f"you picked {u} and the computer chose {c}")


rps(u, c)
    