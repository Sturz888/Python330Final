import random

Ran = random.randrange(1, 11)
guess = input("Guess your number ")
counter = 0

while guess != Ran:

    if int(guess) == Ran:
        counter = counter + 1
        print(str(counter) + " Attempt(s)")
        print("Winner")
        break

    elif int(guess) > Ran:
        counter = counter + 1
        print("Too high")
        guess = input("Guess your number ")

    elif int(guess) < Ran:
        counter = counter + 1
        print("Too Low")
        guess = input("Guess your number ")