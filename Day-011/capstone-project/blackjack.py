import random
import os
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def calculate_score(card_list):
    """Calculate player score from their list of cards and return the number.
    The ace (11) can be either 1 or 11."""

    # Sort card_list to put the ace at the end.
    card_list.sort()
    last_card = card_list[len(card_list) - 1]

    # If the cards total over 21 and the last card is an ace, change the
    # list item from 11 to 1.
    if sum(card_list) > 21 and last_card == 11:
        card_list[len(card_list) - 1] = 1
    return sum(card_list)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def initialize_hand():
    """Return two cards from the deck as a list."""
    card_list = []
    card_list.append(deal_card())
    card_list.append(deal_card())
    return card_list


def play_blackjack():
    """Play a game of Blackjack!"""

    os.system("clear")
    print(logo)

    # Initialize player variables
    player_plays = True
    another_card = True
    player_cards = initialize_hand()
    # DEBUG: Set initial hand to specific cards
    # player_cards = [11, 10]
    player_score = calculate_score(player_cards)

    # Initialize dealer variables
    dealer_plays = True
    dealer_cards = initialize_hand()
    # DEBUG: Set initial hand to specific cards
    # dealer_cards = [10, 11]
    dealer_score = calculate_score(dealer_cards)

    # If one player has a Blackjack, neither gets to draw additional cards.
    blackjack = False
    if player_score == 21 or dealer_score == 21:
        blackjack = True
        player_plays = False
        dealer_plays = False

    print(f"  - Your cards: {player_cards}, current score = {player_score}")
    print(f"  - Dealer's first card: {dealer_cards[0]}")

    # Player turn
    while player_plays and another_card:
        another_card = input("Enter 'y' for another card or 'n' to stand: ").lower()
        if another_card == "y":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"  - Your cards: {player_cards}, current score = {player_score}")
            if player_score > 21:
                player_plays = False
                dealer_plays = False
        elif another_card == "n":
            another_card = False
        else:
            print("Invalid choice, please try again.")

    # Dealer plays if neither has a blackjack and player has not gone bust.
    # Dealer must hit as long as score < 17.
    while dealer_plays and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        if dealer_score > 21:
            dealer_plays = False

    # Determine the winner
    if blackjack:
        if player_score == dealer_score:
            print("\nDraw - Double Blackjack!")
        elif player_score == 21:
            print("\nBlackjack - you win!")
        else:
            print("\nDealer has Blackjack, you lose!")
    elif player_score > 21:
        print("\nBust - you lose!")
    elif dealer_score > 21:
        print("\nDealer busts - you win!")
    elif player_score > dealer_score:
        print("\nYou win!")
    elif dealer_score > player_score:
        print("\nDealer wins!")
    else:
        print("\nIt's a draw!")

    # Print final hand & scores
    print(f"  - Your final hand: {player_cards}, score = {player_score}")
    print(f"  - Dealer's final hand: {dealer_cards}, score = {dealer_score}\n")


play_game = True
while play_game:
    play_game = input("SHALL WE PLAY A GAME (y/n)? ")
    if play_game == "y":
        play_blackjack()
    else:
        play_game = False
        print("\nThank you for playing. End of Line.")
