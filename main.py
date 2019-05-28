class Card(object):
    RANKS = ["Ace of ", "2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "Jack of ", "Queen of ", "King of "]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.RANKS.index(rank) + 1

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    def __cmp__(self, other):
        return cmp(self.value, other.value)

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = ""
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
        
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hand, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

def cardvalue(cr):
    if cr == "Ace of ":
        value = 1
    elif cr == "2 of ":
        value = 2
    elif cr == "3 of ":
        value = 3
    elif cr == "4 of ":
        value = 4
    elif cr == "5 of ":
        value = 5
    elif cr == "6 of ":
        value = 6
    elif cr == "7 of ":
        value = 7
    elif cr == "8 of ":
        value = 8
    elif cr == "9 of ":
        value = 9
    elif cr == "10 of ":
        value = 10
    elif cr == "Jack of ":
        value = 11
    elif cr == "Queen of ":
        value = 12
    elif cr == "King of ":
        value = 13
    else:
        value = 0
    return value

deck1 = Deck()
deck1.populate()
deck1.shuffle()
player1_hand = Hand()
player2_hand = Hand()
hands = [player1_hand, player2_hand]
deck1.deal(hands, per_hand=1)

print("Player1 hand:", player1_hand)
print("Player2 hand:", player2_hand)