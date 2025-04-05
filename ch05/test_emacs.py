from emacs import count_rectangles


def test_count_rectangles_1():
    rectangles = ["*.*"]
    assert count_rectangles(rectangles) == 2


def test_count_rectangles_2():
    rectangles = [
        "*.*",
        "...",
        "*.*",
    ]
    assert count_rectangles(rectangles) == 4


def test_count_rectangles_3():
    rectangles = [
        "***....",
        "***..**",
        ".....**",
        ".***.**",
        ".***...",
        ".***...",
    ]
    assert count_rectangles(rectangles) == 3
