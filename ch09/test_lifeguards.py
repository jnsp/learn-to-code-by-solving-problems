from lifeguards import covered, covered_if_fired


def test_covered_if_fired():
    intervals = [(5, 9), (1, 4), (3, 7)]
    fired = 0
    assert covered_if_fired(intervals, fired) == 6


def test_covered1():
    intervals = [(5, 9), (1, 4), (3, 7)]
    assert covered(intervals) == 7


def test_covered2():
    intervals = [
        (134, 203),
        (186, 288),
        (274, 380),
        (46, 138),
        (373, 451),
    ]
    assert covered(intervals) == 357
