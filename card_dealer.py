from random import *

# List of full deck
deck = ["King Clubs", "Queen Clubs", "Jack Clubs", "10 Clubs", "9 Clubs", "8 Clubs", "7 Clubs", "6 Clubs", "5 Clubs", "4 Clubs", "3 Clubs", "2 Clubs", "Ace Clubs",
        "King Diamonds", "Queen Diamonds", "Jack Diamonds", "10 Diamonds", "9 Diamonds", "8 Diamonds", "7 Diamonds", "6 Diamonds", "5 Diamonds", "4 Diamonds", "3 Diamonds", "2 Diamonds", "Ace Diamonds",
        "King Hearts", "Queen Hearts", "Jack Hearts", "10 Hearts", "9 Hearts", "8 Hearts", "7 Hearts", "6 Hearts", "5 Hearts", "4 Hearts", "3 Hearts", "2 Hearts", "Ace Hearts",
        "King Spades", "Queen Spades", "Jack Spades", "10 Spades", "9 Spades", "8 Spades", "7 Spades", "6 Spades", "5 Spades", "4 Spades", "3 Spades", "2 Spades", "Ace Spades",
        "Joker", "Joker"]


# Player 1 cards handout
player1cards = []
i = 0
while i < 5:
    decklen = len(deck)-1
    card = randint(0, decklen)
    player1cards.append(deck[card])
    deck.remove(deck[card])
    i = i + 1
print(f"player 1 your deck is:", *player1cards, sep=', ')

# Player 2 cards handout
player2cards = []
i = 0
while i < 5:
    decklen = len(deck)-1
    card = randint(0, decklen)
    player2cards.append(deck[card])
    deck.remove(deck[card])
    i = i + 1
print(f"player 2 your deck is:", *player2cards, sep=', ')

# Card in the middle
midcard = []
i = 0
while i < 1:
    decklen = len(deck)-1
    card = randint(0, decklen)
    midcard.append(deck[card])
    deck.remove(deck[card])
    i = i + 1
print(f"The card in the middle is:", *midcard, sep=', ')





f = open("cards.txt", "w")
f.write(str(deck))
f.close()

