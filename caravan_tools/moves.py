from typing import List
from cards import Card

def price(Caravan: List[Card]) -> int:
    count = 0
    temp = 0
    for card in Caravan:
        if not card.isPicture():
            count += temp
            temp = card.nameid + 1
        elif card.name == "King":
            temp *= 2
    count += temp
    return count

def last_nonpic_card(Caravan: List[Card]) -> Card:    #последняя карта не картинка
    last = None
    for card in Caravan:
        if not card.isPicture():
            last = card
    return last

def last_suit_check(Caravan: List[Card]) -> str:     #последняя масть, включая дам
    last = None
    for card in Caravan:
        if not card.isPicture() or card.name == "Queen":
            last = card
    return last.suitid

def direction_check(Caravan: List[Card]) -> str:
    result = "unknown"
    last = Caravan[0]     #последняя карта не картинка
    for card in Caravan:
        if card.name == "Queen":
            if result == "up":
                result = "down"
            elif result == "down":
                result = "up"

        elif not card.isPicture():
            if card.nameid > last.nameid:
                result = "up"
            elif card.nameid < last.nameid:
                result = "down"
            last = card

    return result

def add_card(Caravan: List[Card], card: Card, position: int) -> List[Card]:
    if len(Caravan) != 0 and Caravan[position].isPicture() or position >= len(Caravan) or position < 0:    #защита от дурака
        return Caravan
    if len(Caravan) == 0:
        if not card.isPicture():
            Caravan.append(card)

    elif len(Caravan) == 1:
        if card.isPicture():
            if card.name == "Jack":
                Caravan.pop(0)
            elif card.name == "King":
                Caravan.append(card)
        else:
            if card.name != Caravan[0].name:
                Caravan.append(card)

    else:
        direction = direction_check(Caravan)
        last_card = last_nonpic_card(Caravan)
        last_suit = last_suit_check(Caravan)

        if not card.isPicture():
            if card.name != last_card.name:
                if direction == "unknown":
                    Caravan.append(card)
                elif direction == "up":
                    if card.nameid > last_card.nameid or card.suitid == last_suit:
                        Caravan.append(card)

                elif direction == "down":
                    if card.nameid < last_card.nameid or card.suitid == last_suit:
                        Caravan.append(card)

        elif card.name == "Jack":
            Caravan.pop(position)
            while True:
                try:
                    if Caravan[position].isPicture():
                        Caravan.pop(position)
                    else:
                        break
                except:
                    break
        elif card.name == "Queen":
            Caravan.append(card)
        elif card.name == "King":
            Caravan.insert(position + 1, card)
    return Caravan