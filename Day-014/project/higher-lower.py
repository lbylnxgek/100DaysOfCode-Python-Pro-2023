from art import logo
from art import vs
from game_data import data
import os
import random
DEBUG = False

# Data dictionary item keys:
# "name": "Instagram",
# "follower_count": 346,
# "description": "Social media platform",
# "country": "United States",


def correct_answer(a_followers, b_followers):
    if a_followers > b_followers:
        return "a"
    else:
        return "b"


def random_record():
    """Returns a random data list index"""
    return random.randint(0, len(data) - 1)


def print_game_info(index, index_letter):
    """Prints the game ASCII art (logo or vs) and comparitor details"""
    if  index_letter == "a":
        print(logo)
        print(
            f"Compare A: {data[index]["name"]}, a {data[index]["description"]}, from {data[index]["country"]}"
        )
    else:
        print(vs)
        print(
            f"Against B: {data[index]["name"]}, a {data[index]["description"]}, from {data[index]["country"]}"
        )


def check_guess(a_index, b_index):
    """Returns which has the most followers, a or b.  Returns c if a and b are the same."""
    if data[a_index]["follower_count"] > data[b_index]["follower_count"]:
            return "a"
    elif data[a_index]["follower_count"] < data[b_index]["follower_count"]:
            return "b"
    else:
            return "c"


def play_game(a_index, score):
    """Play the game!  Will call itself recursively as long as the player guesses correctly"""

    print_game_info(a_index, "a")
    if DEBUG:
        print(f"DEBUG: a= {a_index}, followers= {data[a_index]["follower_count"]}")

    b_index = random_record()
    while b_index == a_index:
         b_index = random_record()

    print_game_info(b_index, "b")
    if DEBUG:
        print(f"DEBUG: b= {b_index}, followers= {data[b_index]["follower_count"]}")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    correct_answer = check_guess(a_index=a_index, b_index=b_index)

    # Check for a tie
    if correct_answer == "c":
        os.system("clear")
        print("It's a tie!")
        print(f"Your current score is: {score}")
        a_index = random_record()
        play_game(a_index, score)

    # Determine winner.  If player chooses correctly, keep playing
    if guess == correct_answer:
        score += 1
        a_index = b_index
        os.system("clear")
        print("That's correct, well done!")
        print(f"Your current score is: {score}")
        play_game(a_index, score)
    else:
        os.system("clear")
        print(logo)
        print("Sorry, that's not correct.  Better luck next time.")
        print(f"Your final score is: {score}")


os.system("clear")
score = 0
a_index = random_record()
play_game(a_index, score)
