from .moves import (
    price,
    last_nonpic_card,
    last_suit_check,
    direction_check
)
from .cards import Card

class TestModule:
    def test_price(self):
        Caravan = [Card(2, 3), Card(9, 2), Card(12, 0), Card(11, 3), Card(0, 0)]
        assert price(Caravan) == 24

    def test_direction(self):
        Caravan = [Card(2, 3), Card(9, 2), Card(12, 0), Card(11, 3), Card(0, 0)]
        assert direction_check(Caravan) == "down"

    def test_nonpic(self):
        Caravan = [Card(2, 3), Card(9, 2), Card(12, 0), Card(11, 3)]
        last = last_nonpic_card(Caravan)
        assert last.nameid == 9 and last.suitid == 2

    def test_lsuit(self):
        Caravan = [Card(2, 3), Card(9, 2), Card(12, 0)]
        assert last_suit_check(Caravan) == 2