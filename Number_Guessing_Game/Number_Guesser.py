import random

ans = random.randint(1, 100)

guess = int(input("Guess a Number Between 1 and 100\n"))

while guess != ans:
    if guess > ans:
        guess = int(input("Too High! Guess Again: "))
    else:
        guess = int(input("Too Low! Guess Again: "))

print("You Guessed it! The Number was: ", ans)