from skidesign import cost_for_range


def test_cost_for_range1():
    heights = [20, 4, 1, 24, 21]
    assert cost_for_range(heights) == 18


def test_cost_for_range2():
    heights = [23, 40, 16, 2]
    assert cost_for_range(heights) == 221
