from shuffle import move_first_to_end, move_last_to_start, shuffle, swap_first_and_second


def test_move_first_to_end():
    songs = ["A", "B", "C", "D", "E"]
    assert move_first_to_end(songs) == ["B", "C", "D", "E", "A"]


def test_move_last_to_start():
    songs = ["A", "B", "C", "D", "E"]
    assert move_last_to_start(songs) == ["E", "A", "B", "C", "D"]


def test_swap_first_and_second():
    songs = ["A", "B", "C", "D", "E"]
    assert swap_first_and_second(songs) == ["B", "A", "C", "D", "E"]


def test_shuffle():
    songs = ["A", "B", "C", "D", "E"]
    actions = [(2, 1), (3, 1), (2, 3), (4, 1)]
    assert shuffle(songs, actions) == ["B", "C", "D", "A", "E"]
