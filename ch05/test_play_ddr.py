from play_ddr import hit_combo, points, sort_combos


def test_detect_combo_1():
    moves = "RLUDD"
    combo = "RLU"

    hit = True
    expected_moves = "*DD"

    assert hit_combo(moves, combo) == (hit, expected_moves)


def test_detect_combo_2():
    moves = "UDULRLUDU"
    combo = "UDU"

    hit = True
    expected_moves = "*LRLUDU"

    assert hit_combo(moves, combo) == (hit, expected_moves)


def test_detect_empty_combo():
    moves = "RLUDD"
    combo = ""

    hit = False
    expected_moves = moves

    assert hit_combo(moves, combo) == (hit, expected_moves)


def test_sort_combos():
    moves = "UDULRL"
    combos = ["UDU", "ULR"]

    expected_sorted_combos = ["ULR", "UDU"]

    assert sort_combos(moves, combos) == expected_sorted_combos


def test_sort_combos_longest_first():
    moves = "ULRURURU"
    combos = ["LRURU", "LRUR", "URU"]

    expected_sorted_combos = ["URU", "LRUR", "LRURU"]

    assert sort_combos(moves, combos) == expected_sorted_combos


def test_exclude_combos_not_in_moves():
    moves = "UDULRL"
    combos = ["ULR", "UDU", "NOT-COMBO"]

    expected_sorted_combos = ["ULR", "UDU"]

    assert sort_combos(moves, combos) == expected_sorted_combos


def test_sort_empty_combos():
    moves = "UDULRL"
    combos = []

    assert sort_combos(moves, combos) == []


def test_calculate_points_1():
    moves = "RLUDD"
    combos = {"RLU": 4}

    assert points(moves, combos) == 9


def test_calculate_points_2():
    moves = "UDULRL"
    combos = {"ULR": 3, "UDU": 2}

    assert points(moves, combos) == 8


def test_calculate_points_3():
    moves = "ULRURURU"
    combos = {"LRURU": 500, "LRUR": 750, "URU": 1000}

    assert points(moves, combos) == 508
