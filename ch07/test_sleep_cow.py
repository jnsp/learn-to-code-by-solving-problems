import pytest
from sleepy_cow import count_moves


@pytest.mark.parametrize(
    "locations, expected",
    [
        ((4, 7, 9), (1, 2)),
        ((7, 8, 9), (0, 0)),
        ((5, 6, 10), (2, 3)),
        ((8, 20, 21), (2, 11)),
        ((4, 100, 200), (2, 99)),
        ((30, 50, 53), (2, 19)),
        ((4000, 5000, 5002), (1, 999)),
        ((1, 1000000, 2000000), (2, 999999)),
        ((1, 10000000, 100000000), (2, 89999999)),
        ((1, 500000000, 1000000000), (2, 499999999)),
    ],
)
def test_count_moves(locations, expected):
    assert count_moves(locations) == expected
