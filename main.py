import random

cards = []
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Jack", "Queen", "King", "Ace"]
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
    
player1_hand = []
player2_hand = []

n = 2
l = deck

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

list(chunks(l=deck, n=2))
