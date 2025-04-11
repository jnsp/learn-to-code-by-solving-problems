from city_distance import distances_between_cities, distances_from_origin, read_distances


def test_read_distances(monkeypatch):
    distances = "3 10 12 5"
    monkeypatch.setattr("builtins.input", lambda *_: distances)
    assert read_distances() == [3, 10, 12, 5]


def test_distances_from_origin():
    distances = [3, 10, 12, 5]
    assert distances_from_origin(distances) == [0, 3, 13, 25, 30]


def test_distances_between_cities():
    distances_from_origin = [0, 3, 13, 25, 30]
    expected = [
        [0, 3, 13, 25, 30],
        [3, 0, 10, 22, 27],
        [13, 10, 0, 12, 17],
        [25, 22, 12, 0, 5],
        [30, 27, 17, 5, 0],
    ]
    assert distances_between_cities(distances_from_origin) == expected
