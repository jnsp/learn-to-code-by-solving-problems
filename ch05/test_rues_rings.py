from rues_rings import minimum_roundabout


def test_minimum_roundabout_1():
    routes = {
        1: [4, 5, 2, 6, 3, 2],
        2: [2, 3, 4],
        3: [2, 3, 2, 4],
    }

    assert minimum_roundabout(routes) == (2, [1, 2, 3])


def test_minimum_roundabout_2():
    routes = {
        1: [3, 4],
        2: [4, 2, 4],
        3: [2, 3, 3, 4, 5, 2, 6],
        4: [3, 2, 5, 1, 4],
    }

    assert minimum_roundabout(routes) == (1, [4])
