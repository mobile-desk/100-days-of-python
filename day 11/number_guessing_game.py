# number guessing game

from random import *

number_to_guess = randint(1,100)

tries = 3

def check_guess(user_guess):
    if user_guess == number_to_guess:
        print(f"{user_guess} is correct, you win!!")
        exit()
    elif user_guess > number_to_guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

while tries > 0:
    user_guess = int(input("Guess a number between 1 to 100: "))
    check_guess(user_guess)
    tries -= 1

if tries == 0:
    print(f"You lost, game over! The correct answer was {number_to_guess}")