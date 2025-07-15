from fish import catch_combination, max_catches


def test_max_catches():
    points = (1, 2, 3)
    assert max_catches(points, 2) == (2, 1, 0)


def test_catch_combination():
    points = (1, 2, 3)
    actual = catch_combination(points, 2)
    expected = [(1, 0, 0), (2, 0, 0), (0, 1, 0)]
    assert set(expected) == set(actual)
