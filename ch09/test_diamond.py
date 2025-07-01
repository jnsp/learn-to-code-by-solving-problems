from diamond import max_diamonds


def test_max_diamonds1():
    sizes = [1, 6, 4, 3, 1]
    k = 3
    assert max_diamonds(sizes, k) == 4


def test_max_diamonds2():
    sizes = [6, 3, 9, 7, 10, 2, 1, 1, 5, 10]
    k = 0
    assert max_diamonds(sizes, k) == 2


def test_max_diamonds3():
    sizes = [84, 87, 78, 16, 94, 36, 87, 93, 50, 22, 63, 28, 91, 60, 64, 27, 41, 27, 73, 37]
    k = 20
    assert max_diamonds(sizes, k) == 7
