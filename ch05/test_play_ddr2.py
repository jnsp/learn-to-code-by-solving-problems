from play_ddr2 import points


def test_points_1():
    moves = "RLUDD"
    combos = {"RLU": 4}
    assert points(moves, combos) == 9


def test_point_2():
    moves = "UDULRL"
    combos = {"ULR": 3, "UDU": 2}
    assert points(moves, combos) == 8


def test_points_3():
    moves = "ULRURURU"
    combos = {"LRURU": 500, "LRUR": 750, "URU": 1000}
    assert points(moves, combos) == 508
