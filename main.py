import random

cards = []
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["J", "Q", "K", "A"]
deck = []

for i in range(2,11):
    cards.append(str(i))
    
for r in range(4):
    cards.append(ranks[r])
    
for k in range(4):
    for l in range(13):
        card = (cards[l] + " of " + suits[k])
        deck.append(card)

random.shuffle(deck)
    
for d in range(52):
    print(deck[d])