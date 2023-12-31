import os
from art import logo

bidders = {}


def clear_screen():
    os.system("clear")
    print(logo)
    print("\nWelcome to the secret auction.")


more_bidders = "y"
# Bidders loop
while more_bidders == "y":
    clear_screen()
    bidder_name = input("What is your name? ")
    bidder_amount = input("what is your bid? $")
    # Add bidder_name & bidder_amount to bidders dictionary
    # Rember to covert the bidder_amout to an integer
    bidders[bidder_name] = int(bidder_amount)
    more_bidders = input(
        "If there are more bidders, press 'y'. Otherwise press any key to finish the auction: "
    ).lower()

max_bid = 0
max_bidder = ""
# Determine who had the highest bid
for bidder in bidders:
    if bidders[bidder] > max_bid:
        max_bid = bidders[bidder]
        max_bidder = bidder

clear_screen()
# DEBUG:
# print(bidders)
print(f"\nBidder {max_bidder} won the auction with a bid of ${max_bid}.")
