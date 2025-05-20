# Guess the Number game

import random

# Generating a random number between 1 and 100
secret_number = random.randint(1, 100)

guess = None

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100. Try to guess it!")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed the number correctly.")
    except ValueError:
        print("Invalid input. Please enter a number.")

