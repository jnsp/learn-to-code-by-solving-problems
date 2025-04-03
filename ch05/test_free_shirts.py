from free_shirts import laundry


def test_laundry_1():
    n_shirts = 1
    days = 10
    event_days = [10]

    assert laundry(n_shirts, days, event_days) == 9


def test_laundry_2():
    n_shirts = 1
    days = 10
    event_days = [2, 9, 5]

    assert laundry(n_shirts, days, event_days) == 3
