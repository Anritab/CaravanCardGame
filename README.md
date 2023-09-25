# why?
This Python package will help you implement the Caravan card game.

The most important thing it does is add cards to the caravan pile using the "add_card" method. If it is impossible to add a card, the caravan does not change.

It also has several auxiliary methods, such as "price" - which allows you to estimate the cost of a caravan, or "direction_check", which allows you to determine the direction of the stack (increasing or descending).

Playing cards are implemented using the "Card" class, which contains the name of the card and its suit.

So far this package does not contain manipulations with the Joker card, but it will be added in the future. (maybe)

# jack add instruction

You must enter a list of cards [name1, suit1, name2, suit2...], where name (1-13) are in odd places, and suit (1-4) are in even places. The sequence of cards must be a valid caravan. (there should be no jacks in it, and the number card should come first).

You also need to select the card on which you want to place the jack. Jack can only be placed on number cards.

For example, you can use `python -m caravanassets -cards "[1, 2, 3, 4, 13, 2, 4, 2]"` 
output:
`Three Clubs
King Diamonds
Four Diamonds`

by default the program uses jack on the first card

but if you need to use it on other card, you can use
`python -m caravanassets -cards "[1, 2, 3, 4, 13, 2, 4, 2]" -addj 2` 
output:
`Ace Diamonds
Four Diamonds`

the jack removed the second card, and all the picture cards on it.

# input

-cards / --caravan (necessary)

-addj / --addjack (not necessary)

# installation
`pip install caravanassets`

# tests

you can run tests using `pytest -q caravanassets/module_test.py`
