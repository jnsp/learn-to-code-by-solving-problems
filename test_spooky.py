import pytest

from spooky import spooky


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "spoky"),
        (2, "spooky"),
        (3, "spoooky"),
        (4, "spooooky"),
        (5, "spoooooky"),
    ],
)
def test_spooky(n, expected):
    assert spooky(n) == expected
