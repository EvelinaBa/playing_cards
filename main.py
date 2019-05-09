import random
from random import shuffle

suits = ["spade","club","heart","diamond"]
rank = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]

# suit1 = random.choice(suit)
# rank1 = random.choice(rank)

card1 = ("spade", 2)
all_cards = []

for suit in suits:
    for card in cards:
        card = (suit, card)
        all_cards.append(card)

shuffle(all_cards)
print(all_cards)