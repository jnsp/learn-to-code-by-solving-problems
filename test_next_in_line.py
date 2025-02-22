import pytest

from next_in_line import next_in_line


@pytest.mark.parametrize(
    "youngest_age, middle_age, expected",
    [
        (1, 2, 3),
        (10, 10, 10),
        (12, 15, 18),
    ],
)
def test_next_in_line(youngest_age, middle_age, expected):
    assert next_in_line(youngest_age, middle_age) == expected
