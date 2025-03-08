from winning_score import winning_score


def test_B_wins():
    assert winning_score(10, 3, 7, 8, 9, 6) == "B"


def test_A_wins():
    assert winning_score(10, 9, 7, 8, 9, 7) == "A"


def test_Tie():
    assert winning_score(7, 3, 0, 6, 4, 1) == "T"
