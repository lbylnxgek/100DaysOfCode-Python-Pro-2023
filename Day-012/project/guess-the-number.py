import random
from art import logo


def check_guess(player_guess, random_number):
    """Check player guess against number, return low, high or match"""
    if player_guess < random_number:
        return "low"
    elif player_guess > random_number:
        return "high"
    else:
        return "match"


# Print logo and welcome information
print(logo)
print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Pick a random number
number = random.randint(1, 100)
# DEBUG: Print random number
print(f"DEBUG: The number is {number}.")

# Prompt user for a difficulty level, set guesses_remaining
difficulty_level = input("Choose a difficulty level.  Type 'easy' or 'hard': ").lower()
if difficulty_level == "easy":
    guesses_remaining = 10
else:
    guesses_remaining = 5

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
