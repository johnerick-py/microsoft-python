import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards = []
baralho = []
count = 0

for suit in suits:
    for rank in ranks:
        cards = rank + ' of ' + suit
        baralho.append(cards)

random.shuffle(baralho)
print(f'There are {len(baralho)} cards in the deck.')
print('Dealing...')

hand = random.choices(baralho, k=6)
while count < 5:
    count = count + 1
    del baralho[0]

print(f'There are {len(baralho)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)


# Gabarito

# import random
#
# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
# deck = []
#
# for  suit in suits:
#   for rank in ranks:
#     deck.append(f'{rank} of {suit}')
#
# print(f'There are {len(deck)} cards in the deck.')
#
# print('Dealing ...')
#
# hand = []
#
# while len(hand) < 5:
#     card = random.choice(deck)
#     deck.remove(card)
#     hand.append(card)
#
# print(f'There are {len(deck)} cards in the deck.')
# print('Player has the following cards in their hand:')
# print(hand)