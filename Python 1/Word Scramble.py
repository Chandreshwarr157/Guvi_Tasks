import random  # Importing the random module for word scrambling

# List of words for the game
words = ['Python', 'JavaScript', 'Java', 'Automation', 'Pytest', 'Guvi', 'Selenium']

# Choose a random word from the list
original_word = random.choice(words)

# Scramble the word
scrambled_word = ''.join(random.sample(original_word, len(original_word)))

print("Welcome to the Word Scramble game!")
print(f"Unscramble this word: {scrambled_word}")

# Allow multiple attempts
attempts = 3  # Limit the number of guesses
for attempt in range(attempts):
    guess = input("Enter your guess: ").strip()

    if guess.lower() == original_word.lower():  # Case-insensitive check
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        print("Wrong guess! Try again.")

if guess.lower() != original_word.lower():
    print(f"Better luck next time! The correct word was: {original_word}")