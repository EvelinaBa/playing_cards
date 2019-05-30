import random
import itertools


deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'],['Clubs', 'Diamonds', 'Hearts', 'Spades']))
random.shuffle(deck)
print(deck)


print(len(deck))

#Deal cards to each player
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

# One card is revealed for each player


#Values are compared

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


#cardvalue(deck[2][0]) < cardvalue(deck[4][0])

win_count1 = 0
win_count2 = 0

for i in range(len(player1_hand)):
 #cardvalue(player1_hand[i][0])
 #cardvalue(player2_hand[i][0])

 #print(cardvalue(player1_hand[i][0]))
 #print(cardvalue(player2_hand[i][0]))

 print('\n' ,player1_hand[i], ' vs ', player2_hand[i])


 if cardvalue(player1_hand[i][0]) > cardvalue(player2_hand[i][0]):
   win_count1 +=1
   print('Player1 wins\n')
 elif cardvalue(player1_hand[i][0]) == cardvalue(player2_hand[i][0]):
   print('Draw\n')
 else:
   win_count2 +=1
   print('Player2 wins\n')

print(win_count1, win_count2)

if win_count1 > win_count2:
 print('pl1 wins')
elif win_count1 == win_count2:
 print('draw')
else:
 print('pl2 wins')