from patkice import find_start, voyage


def test_find_start1():
    map = [
        "..>>>v",
        ".o^..v",
        ".v.<.v",
        ".>>^.v",
        ".x<<<<",
        "......",
    ]

    assert find_start(map) == [1, 1]


def test_find_start2():
    map = [
        "v<<<<",
        ">v.>^",
        "v<.o.",
        ">>v>v",
        "..>>x",
    ]

    assert find_start(map) == [2, 3]


def test_voyage1():
    map = [
        "..>>>v",
        ".o^..v",
        ".v.<.v",
        ".>>^.v",
        ".x<<<<",
        "......",
    ]

    assert voyage(map) == (":)", "E")


def test_voyage2():
    map = [
        "v<<<<",
        ">v.>^",
        "v<.o.",
        ">>v>v",
        "..>>x",
    ]

    assert voyage(map) == (":)", "S")


def test_voyage3():
    map = [
        "x>.",
        ".o^",
        "^<.",
    ]

    assert voyage(map) == (":(",)
