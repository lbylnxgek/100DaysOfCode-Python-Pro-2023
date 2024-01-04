import random
from art import logo

# Set global constants here, as it makes changing the difficulty easy since
# no code modification is necessary.
EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5


def check_guess(player_guess, random_number):
    """Check player guess against number, return low, high or match"""
    if player_guess < random_number:
        return "low"
    elif player_guess > random_number:
        return "high"
    else:
        return "match"


def set_difficulty_level():
    level = input("Choose a difficulty level.  Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_GUESSES
    else:
        return HARD_LEVEL_GUESSES


# Print logo and welcome information
print(logo)
print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Pick a random number
number = random.randint(1, 100)
# DEBUG: Print random number
# print(f"DEBUG: The number is {number}.")

# Set number of guesses
guesses_remaining = set_difficulty_level()

game_over = False
while not game_over:
    print(f"You have {guesses_remaining} guesses remaining.")
    guess = int(input("What is your guess? "))
    result = check_guess(player_guess=guess, random_number=number)
    if result == "low":
        print("Too low.")
        guesses_remaining -= 1
    elif result == "high":
        print("Too high.")
        guesses_remaining -= 1
    elif result == "match":
        print(f"Winner, winner, chicken dinner!  The number was {number}.")
        game_over = True
    if guesses_remaining == 0:
        print(f"\nYou are out of guesses, the number was {number}.")
        game_over = True
