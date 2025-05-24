from bard import get_evenings, villagers_with_all_songs


def test_villagers_with_all_songs_1():
    evenings = [
        [1, 2],
        [2, 3, 4],
        [4, 2, 1],
    ]

    assert villagers_with_all_songs(evenings) == [1, 2, 4]


def test_villagers_with_all_songs_2():
    evenings = [
        [1, 3, 5, 4],
        [5, 6],
        [6, 7, 8],
        [6, 2],
        [2, 6, 8, 1],
    ]

    assert villagers_with_all_songs(evenings) == [1, 2, 6, 8]


def test_villagers_with_all_songs_3():
    evenings = [
        [1, 3],
        [2, 1],
        [2, 1, 4, 5],
    ]

    assert villagers_with_all_songs(evenings) == [1]


def test_get_evenings(monkeypatch):
    inputs = iter(["4", "3", "2 1 2", "3 2 3 4", "3 4 2 1"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    expected = [
        [1, 2],
        [2, 3, 4],
        [4, 2, 1],
    ]
    assert get_evenings() == expected
