#for now only for debug
from moves import *
from cards import *

deck = list()
for name in range(13):
    for suit in range(4):
        deck.append(Card(name, suit))
car = [deck[2], deck[10], deck[1]]
car = add_card(car, deck[5], 1)
car = add_card(car, deck[47], 1)
car = add_card(car, deck[27], 1)
car = add_card(car, deck[51], 1)
car = add_card(car, deck[49], 1)
car = add_card(car, deck[20], 1)
car = add_card(car, deck[50], 3)
car = add_card(car, deck[25], 1)
for card in car:
    print(card.name, card.suit)
print(direction_check(car))
print(price(car))