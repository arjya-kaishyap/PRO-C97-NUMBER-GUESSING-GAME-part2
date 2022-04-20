
import random
print("Number guessing game")
number = random.randint(1,9)
changes = 1
print("Guess a number (between 1 and 9): ")

while changes < 5:

    guess = int(input("Enter your guess:- "))


    if guess == number:
        print("Congratulation You Won!!!")
        break

    elif guess < number:
        print("Your guess was too low:Guess a number higher than that",guess)

    else:
        print("Your guess was too high:Guess a number lower than that",guess)
    changes += 1

    if not changes < 5:
        print("You Lose!!! The number is",number)