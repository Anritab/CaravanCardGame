#for now only for debug
from .moves import *
from .cards import *

def main():
    print("try to add some cards")
    while True:
        print("you have to choose card name (1-13) where 1 - ace, 11 - jack, 12 - queen, 13 - king, others just numbers")
        name = int(input()) - 1
        print("now choose card suit (1-4)")
        suit = int(input()) - 1
        print("and again 4 more times")
        deck = []
        new = Card(name, suit)
        deck = add_card(deck, new, 0)
        for _ in range(4):
            print("enter name (1-13)")
            name = int(input()) - 1
            print("enter suit (1-4)")
            suit = int(input()) - 1
            print("choose a position (it matters only for jack and king, put 0 if you dont want) (0-length)")
            pos = int(input())
            new = Card(name, suit)
            deck = add_card(deck, new, pos)

        print("Your caravan:")
        for card in deck:
            print(card.name, card.suit)


        print("Do you want to try again? (y/n)")
        if input() == "n":
            break
if __name__ == "__main__":
    main()