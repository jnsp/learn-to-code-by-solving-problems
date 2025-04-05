from tides import difference


def test_valid_tides():
    tides = [2, 1, 3, 5, 10]
    assert difference(tides) == 9


def test_invalid_tides():
    tides = [1, 2, 5, 4, 9]
    assert difference(tides) == "unknown"
