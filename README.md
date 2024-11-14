# Blackjack Card Game


For this project, I'll be creating a simplified version of the popular casino game, Blackjack (also called 21). Some of the advanced rules like splitting, doubling down, and insurance won't be included in this version.

In this game, there will be two players: myself (the player) and the dealer. The goal is to win as much money as possible by competing against the dealer. The player’s objective is to end each round with a hand value higher than the dealer’s, but without going over 21. Card values are as follows: face cards (King, Queen, Jack) count as 10, an Ace can be worth 1 or 11 (depending on what benefits the player), and all other cards are worth their number value. For instance, a hand with a three, two, king, and ace would total 16 (since the ace counts as 1 here to avoid busting). A bust occurs when the hand value exceeds 21, resulting in an automatic loss of the player’s bet.

The game play consists of several steps per round:

1. **Betting**: The player places a bet, ranging between $1 and the total amount of money they have.

2. **Dealing**: Both the player and dealer are dealt two cards; the player’s cards are face up, while the dealer’s cards include one face down.

3. **Player’s Choice**: The player decides to either hit (receive another card) or stay. If the player hits and their hand goes over 21, they bust and lose the round. The player can keep hitting until they decide to stay or bust.

4. **Dealer’s Turn**: The dealer then reveals their hidden card and follows preset rules to hit or stay: the dealer must hit until reaching a hand value of at least 17 and busts if exceeding 21.

After both turns, the hand with the highest value not over 21 wins:
- If the player wins, they receive double their bet.
- If the dealer wins, the dealer takes the player’s bet.
- A tie returns the original bet to the player.
  
A "blackjack" (a hand value of 21 with the first two cards) pays the player one and a half times their original bet if the dealer doesn’t also have a blackjack. The game uses one deck of 52 cards (four suits of 13 cards each). Each round begins by shuffling the deck.

The game will start with $500 for the player, and they can continue playing until they either choose to stop or run out of money.

For this game we will use one deck of 52 cards having 4 suits and 13 cards within each suit (2 - 9, King (K), Queen (Q), Jack (J), Ten (T), Ace (A)). To represent the suits of cards you can use some special Python unicode values. These will only work in Python version 3 and may not work on all operating systems.

>>> print(u"\u2666") # diamond
♦
>>> print(u"\u2665") # heart
♥
>>> print(u"\u2663") # club
♣
>>> print(u"\u2660") # spade
♠

----------------------------------------------------------------------------------------------------------------------------

Sample Program Execution
Welcome to Blackjack!

You are starting with $500. Would you like to play a hand? yes
Place your bet: -5
The minimum bet is $1.
Place your bet: 2.50
You are dealt: 2♦, A♥
The dealer is dealt: 7♦, Unknown
Would you like to hit or stay? nothing
That is not a valid option. 
Would you like to hit or stay? hit
You are dealt: K♠
You now have: 2♦, A♥, K♠
Would you like to hit or stay? hit
You are dealt: Q♣
You now have: 2♦, A♥, K♠, Q♣
Your hand value is over 21 and you lose $2.50 :(

You are starting with $497.50. Would you like to play a hand? yes
Place your bet: 100
You are dealt: K♦, A♥
The dealer is dealt: J♦, Unknown
The dealer has: J♦, T♥
Blackjack! You win $150 :)

You are starting with $647.50. Would you like to play a hand? yes
Place your bet: 2500
You do not have sufficient funds.
Place your bet: 647.50
You are dealt: 2♦, 4♥
The dealer is dealt: A♠, Unknown
Would you like to hit or stay? hit
You are dealt: Q♦
You now have: 2♦, 4♥, Q♦
Would you like to hit or stay? stay
The dealer has: A♠, 3♥
The dealer hits and is dealt: J♣
The dealer has: A♠, 3♥, J♣
The dealer busts, you win $647.50 :)

You are starting with $1295. Would you like to play a hand? yes
Place your bet: 295
You are dealt: T♦, T♥
The dealer is dealt: 7♠, Unknown
Would you like to hit or stay? stay
The dealer has: 7♠, 3♥
The dealer hits and is dealt: A♠
The dealer has: 7♠, 3♥, A♠
The dealer stays.
The dealer wins, you lose $295 :(

You are starting with $1000. Would you like to play a hand? yes
Place your bet: 1000
You are dealt: Q♦, K♥
The dealer is dealt: 9♠, Unknown
Would you like to hit or stay? stay
The dealer has: 9♠, A♥
The dealer stays.
You tie. Your bet has been returned.

You are starting with $1000. Would you like to play a hand? yes
Place your bet: 1000
You are dealt: 4♠, 7♣
The dealer is dealt: 2♥, Unknown
Would you like to hit or stay? hit
You are dealt: 9♦
You now have: 4♠, 7♣, 9♦
Would you like to hit or stay? stay
The dealer has: 2♥, 6♥
The dealer hits and is dealt: A♠
The dealer has: 2♥, 6♥, A♠
The dealer stays.
You win $1000!

You are starting with $2000. Would you like to play a hand? yes
Place your bet: 2000
You are dealt: 3♦, 5♥
The dealer is dealt: 8♠, Unknown
Would you like to hit or stay? stay
The dealer has: 8♠, 9♥
The dealer stays.
The dealer wins, you lose $2000 :(

You've ran out of money. Please restart this program to try again. Goodbye.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
