NAMES = ("Ace",
        "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
         "Jack", "Queen", "King")
SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")


class Card:

    global NAMES, SUITS

    def __init__(self, nameid, suitid):
        self.name = NAMES[nameid]
        self.suit = SUITS[suitid]
        self.nameid = nameid
        self.suitid = suitid

    def isPicture(self):        #является ли карта "картинкой"
        if self.name == "Jack" or self.name == "Queen" or self.name == "King":
            return True
        return False