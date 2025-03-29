from cezar import numbers_cards


def test_numbers_cards():
    drawn_cards = [2, 3, 2, 3, 2, 3]
    assert numbers_cards(drawn_cards) == (32, 14)
