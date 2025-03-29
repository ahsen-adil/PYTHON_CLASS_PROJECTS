import random

# List of words
words = ["mobile", "computer", "laptop"]

# Randomly select a word
word = random.choice(words)

# Initialize game variables
total_chances = 7
guessed_word = "-" * len(word)

# Main game loop
while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").lower()  # Convert input to lowercase to match the word

    if letter in word:
        # Update guessed_word with the correctly guessed letter
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]

        # Check if the word is fully guessed
        if guessed_word == word:
            print("Congratulations! You won!!!")
            break
    else:
        total_chances -= 1
        print("Incorrect guess.")
        print("The remaining chances are:", total_chances)

# Check if the player lost
if guessed_word != word:
    print("Game over.")
    print("You lose.")
    print("All the chances are exhausted.")
    print("The correct word was:", word)