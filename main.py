import random
import itertools

# Create a shuffled deck of cards
deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10',
                               'Jack', 'Queen', 'King', 'Ace'], ['Clubs', 'Diamonds', 'Hearts', 'Spades']))
random.shuffle(deck)

# Split deck into two parts
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

# Define card values
def cardvalue(cr):
    if cr == 'Ace':
        value = 1
    elif cr == '2':
        value = 2
    elif cr == '3':
        value = 3
    elif cr == '4':
        value = 4
    elif cr == '5':
        value = 5
    elif cr == '6':
        value = 6
    elif cr == '7':
        value = 7
    elif cr == '8':
        value = 8
    elif cr == '9':
        value = 9
    elif cr == '10':
        value = 10
    elif cr == 'Jack':
        value = 11
    elif cr == 'Queen':
        value = 12
    elif cr == 'King':
        value = 13
    else:
        raise "unknown value"
    return value


# Count how many rounds a player wins
win_count1 = 0
win_count2 = 0


# Reveal a card for each player until cards run out and compare the values of the cards
for i in range(len(player1_hand)):

    print(player1_hand[i], ' vs ', player2_hand[i])

    if cardvalue(player1_hand[i][0]) > cardvalue(player2_hand[i][0]):
        win_count1 += 1
        print('Player1 wins!')
    elif cardvalue(player1_hand[i][0]) == cardvalue(player2_hand[i][0]):
        print('Draw!')
    else:
        win_count2 += 1
        print('Player2 wins!')


# Reveal the total count of wins for each player
print('Player1 win count:', win_count1) 
print('Player2 win count:', win_count2)

# Determine the winner of the game
if win_count1 > win_count2:
    print('Player1 wins the game!')
elif win_count1 == win_count2:
    print('Draw!')
else:
    print('Player2 wins the game!')
