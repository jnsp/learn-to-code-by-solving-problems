import pytest

from new_hope import new_hope


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "A long time ago in a galaxy away..."),
        (1, "A long time ago in a galaxy far away..."),
        (2, "A long time ago in a galaxy far, far away..."),
        (3, "A long time ago in a galaxy far, far, far away..."),
        (4, "A long time ago in a galaxy far, far, far, far away..."),
        (5, "A long time ago in a galaxy far, far, far, far, far away..."),
    ],
)
def test_new_hope(n, expected):
    assert new_hope(n) == expected
