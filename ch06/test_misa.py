from misa import Church


def test_read_grid(monkeypatch):
    church = Church()
    inputs = [
        "2 3",
        "..o",
        "o..",
    ]
    monkeypatch.setattr("builtins.input", lambda *_: inputs.pop(0))

    expected = [
        "..o",
        "o..",
    ]

    church.read_benches()
    assert church.n_rows == 2
    assert church.n_columns == 3
    assert church.benches == expected


def test_neighbors_corners():
    church = Church(2, 3, ["..o", "o.."])
    assert church.get_neighbors_positions((0, 0)) == {(0, 1), (1, 1), (1, 0)}
    assert church.get_neighbors_positions((1, 2)) == {(0, 1), (0, 2), (1, 1)}


def test_neighbors_centers():
    church = Church(4, 4, ["...."] * 4)
    assert church.get_neighbors_positions((1, 1)) == {
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    }
    assert church.get_neighbors_positions((2, 2)) == {
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    }


def test_is_occupied():
    church = Church(2, 3, ["..o", "o.."])
    assert not church.is_occupied((0, 0))
    assert church.is_occupied((0, 2))


def test_handshakes_not_full():
    church = Church(2, 3, ["..o", "o.."])
    assert church.handshakes() == 2


def test_handshakes_full():
    church = Church(2, 2, ["oo", "oo"])
    assert church.handshakes() == 6
