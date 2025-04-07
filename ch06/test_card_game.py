from card_game import no_high, play_game


def test_no_high_true():
    deck = ["three", "seven"]
    assert no_high(deck)


def test_no_high_false():
    deck = ["eight", "ten", "jack"]
    assert not no_high(deck)


def test_play_game():
    deck = ["three", "seven", "queen", "eight", "five", "ten"]
    point_logs = [("A", 2)]
    points = {"A": 2, "B": 0}
    assert play_game(deck) == (point_logs, points)
