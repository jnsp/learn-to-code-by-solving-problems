from when_you_eat_smarties import calculate_time, gather_smarties


def test_add_red():
    container = {"red": 0}
    gather_smarties(container, "red")
    assert container == {"red": 1}


def test_calculate_time():
    container = {"orange": 8, "red": 3}
    assert calculate_time(container) == 74
