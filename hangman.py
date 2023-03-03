import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "indigo", "jujube", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "xylocarp", "yellowtail", "zucchini"]

# Choose a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the letters in the word
display = ["_"] * len(word)

# Keep track of the guesses and the number of incorrect guesses
guesses = []
incorrect_guesses = 0

# Main loop of the game
while True:
    # Print the current state of the word
    print(" ".join(display))
    
    # Prompt the player to make a guess
    guess = input("Enter a letter: ").lower()
    
    # Check if the guess is valid
    if not guess.isalpha():
        print("Invalid input. Please enter a letter.")
        continue
    elif guess in guesses:
        print("You already guessed that letter. Please try again.")
        continue
    
    # Add the guess to the list of guesses
    guesses.append(guess)
    
    # Check if the guess is correct
    if guess in word:
        # Replace the underscores with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        # Increment the number of incorrect guesses
        incorrect_guesses += 1
        
        # Check if the player has lost
        if incorrect_guesses == 6:
            print("You have run out of guesses. The word was", word)
            break
    
    # Check if the player has won
    if "_" not in display:
        print("Congratulations! You guessed the word", word)
        break
