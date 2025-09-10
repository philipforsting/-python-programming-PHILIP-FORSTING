import random

randInt = random.randint(1,100)
guess = 0
nrOfGuesses = 0

while True:
    guess = int(input("Guess randomized number "))
    if randInt == guess:
        print(f"Correct guess. Number of guesses: {nrOfGuesses} Game ends")
        break

    if guess < randInt:
        print(f"Guess higher")
    else:
        print(f"Guess lower")

    nrOfGuesses += 1

