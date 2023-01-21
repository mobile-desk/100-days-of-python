from random import *
list = ["python", "program", "function", "game", "computer", "language", "development", "code"]



def select_word():
    return choice(list)
      

def hangman():
    user = []
    word_to_guess = []
    word = select_word()

    for ss in word:
        word_to_guess.append(ss)
    for i in word:
        user.append("*")
    

    #game logic
    guesses = 6
    while guesses > 0:
        v = input("pick a letter: ")
        for i in word_to_guess:
            if i == v:
                b = word_to_guess.index(i)
                user[b] = v
        if v not in word_to_guess:    
            guesses -= 1

        if "*" not in user:
            print("You won")
            exit()

        print(user)


        if guesses == 0 or guesses < 0:
            print(f"You lost, the word was {word}")
        



    


hangman()