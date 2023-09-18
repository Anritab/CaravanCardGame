import argparse
import json
from .moves import (
    price,
    last_nonpic_card,
    last_suit_check,
    direction_check,
    add_card
)
from .cards import (
    NAMES,
    SUITS,
    Card
)
def get_args():

    parser = argparse.ArgumentParser(prog="Helper", description="Описание программы")

    parser.add_argument("-cards", "--caravan", type=json.loads, help="Список карт в формате [name1, suit1, name2, suit2...], name (1-13), suit (1-4)", required=True)
    parser.add_argument("-addj", "--addjack", type=int, help="Положить вальта на карту (1-(len(caravan) // 2))", default="1", required=False)

    return parser.parse_args()

__all__ = [
    "price",
    "last_nonpic_card",
    "last_suit_check",
    "direction_check",
    "add_card",
    "NAMES",
    "SUITS",
    "Card"
]