from spindie import is_possible


def test1():
    integers = [26, 5, 11]
    targets = [407, 962, 455, 21, 902]
    assert is_possible(integers, targets) == "TTFTF"


def test2():
    integers = [23, 74, 7, 64, 47]
    targets = [128605, 205, 2162, 2709, 71346]
    assert is_possible(integers, targets) == "FFTFF"


def test3():
    integers = [23, 61, 77, 83, 12, 92, 1, 7, 65]
    targets = [72900, 144, 5704, 145, 6370]
    assert is_possible(integers, targets) == "FTTTF"
