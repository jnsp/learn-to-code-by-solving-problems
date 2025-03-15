from rijeci import display


def test_press_once():
    assert display(1) == (0, 1)
    assert display(4) == (2, 3)
    assert display(10) == (34, 55)
