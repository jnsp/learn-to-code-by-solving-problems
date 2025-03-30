from wild_ride import waiting_days


def test_waiting_days1():
    play_days = 3
    shoppings = ["E", "B", "E", "B", "E"]

    assert waiting_days(play_days, shoppings) == 2


def test_waiting_days2():
    play_days = 2
    shoppings = ["B", "E", "E", "E"]

    assert waiting_days(play_days, shoppings) == 0
