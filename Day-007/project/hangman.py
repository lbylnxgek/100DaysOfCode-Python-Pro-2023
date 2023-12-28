import random
import hangman_words
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

stages = hangman_art.stages
end_of_game = False
lives = 6
guessed_letters = ""

print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    # If the user has entered a letter they've already guessed, print the letter and let them know
    if guess in guessed_letters:
        print(f"You already guessed {guess}, please try again.")
    else:
        guessed_letters += guess
        # print(f"Guessed letters: {guessed_letters}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"Letter {guess} is not in the word.  You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])