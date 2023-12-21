rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Welcome to Rock, Paper, Scissors - Let's get ready to rumble!")
user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Print ASCII art based on user's choice
print("\n")
if user == 0:
    print("You chose Rock.")
    print(rock)
elif user == 1:
    print("You chose Paper.")
    print(paper)
elif user == 2:
    print("You chose Scissors.")
    print(scissors)
else:
    print("Invalid choice. Please try again.")
    quit()

# Use random function to select computer's choice
computer = random.randint(0, 2)

# Print computer's choice
if computer == 0:
    print("Computer chooses Rock.")
    print(rock)
elif computer == 1:
    print("Computer chooses Paper.")
    print(paper)
elif computer == 2:
    print("Computer chooses Scissors.")
    print(scissors)

# Check for a draw
if user == computer:
  print("It's a draw!")
  quit()
  
# Determine who won
if user == 0:
    if computer == 1:
        print("Computer wins!")
    else:
        print("You win!")
elif user == 1:
    if computer == 2:
        print("Computer wins!")
    else:
        print("You win!")
elif user == 2:
    if computer == 0:
        print("Computer wins!")
    else:
        print("You win!")
