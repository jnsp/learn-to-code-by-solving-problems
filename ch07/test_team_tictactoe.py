import pytest
from team_tictactoe import count_winners


@pytest.mark.parametrize(
    "board, expected",
    [
        (("COW", "XXO", "ABC"), (0, 2)),
        (("RRR", "RRR", "RRR"), (1, 0)),
        (("XYZ", "XYZ", "XYX"), (2, 2)),
        (("QQQ", "QPQ", "QQQ"), (1, 1)),
        (("ABA", "BAB", "ABA"), (1, 1)),
        (("EAT", "COW", "YUM"), (0, 0)),
        (("AXY", "XAX", "ZZB"), (0, 3)),
    ],
)
def test_count_winners(board, expected):
    assert count_winners(board) == expected
