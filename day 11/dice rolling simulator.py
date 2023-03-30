from random import *

rolls = int(input("How many times do you want to roll the die: "))

total = []

while rolls > 0:
    r = randint(1,6)
    total.append(r) 
    rolls -= 1

print(total)