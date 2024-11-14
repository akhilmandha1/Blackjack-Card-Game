
import random

# Constants for card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Suits using Unicode symbols
SUITS = ['\u2660', '\u2663', '\u2665', '\u2666']  # spades, clubs, hearts, diamonds

# Initialize deck
def create_deck():
    return [(rank, suit) for rank in CARD_VALUES.keys() for suit in SUITS]

# Shuffle deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Calculate hand value
def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display hand
def display_hand(hand):
    return ", ".join(f"{card[0]}{card[1]}" for card in hand)

# Game main loop
def play_blackjack():
    money = 500
    deck = create_deck()

    print("Welcome to Blackjack!")

    while money > 0:
        print(f"\nYou are starting with ${money}. Would you like to play a hand? (yes or no)")
        if input().lower() != 'yes':
            break

        # Place bet
        while True:
            try:
                bet = float(input("Place your bet: "))
                if bet < 1:
                    print("The minimum bet is $1.")
                elif bet > money:
                    print("You do not have sufficient funds.")
                else:
                    break
            except ValueError:
                print("Please enter a valid amount.")

        shuffle_deck(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print(f"\nYou are dealt: {display_hand(player_hand)}")
        print(f"The dealer is dealt: {dealer_hand[0][0]}{dealer_hand[0][1]}, Unknown")

        # Player turn
        while True:
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print(f"Your hand value is over 21 and you lose ${bet} :(")
                money -= bet
                break

            print("Would you like to hit or stay?")
            action = input().lower()
            if action == "hit":
                player_hand.append(deck.pop())
                print(f"You are dealt: {display_hand(player_hand)}")
            elif action == "stay":
                break
            else:
                print("That is not a valid option.")

        # Dealer turn if player didn't bust
        if player_value <= 21:
            print(f"\nThe dealer has: {display_hand(dealer_hand)}")
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                print(f"The dealer hits and is dealt: {display_hand(dealer_hand)}")

            dealer_value = calculate_hand_value(dealer_hand)
            if dealer_value > 21:
                print(f"The dealer busts, you win ${bet}!")
                money += bet
            elif dealer_value > player_value:
                print(f"The dealer wins, you lose ${bet} :(")
                money -= bet
            elif dealer_value < player_value:
                print(f"You win ${bet}!")
                money += bet
            else:
                print("You tie. Your bet has been returned.")

    print(f"\nYou've ran out of money. Please restart this program to try again. Goodbye.")

# Run the game
play_blackjack()
