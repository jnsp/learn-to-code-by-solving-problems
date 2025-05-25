from mode import find_modes


def test_find_modes():
    values = [9, 2, 9, 6, 8, 7, 1, 3, 9, 6]
    assert find_modes(values) == [9]
