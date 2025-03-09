from occupy_parking import occupy_parking


def test_occupy_parking():
    assert occupy_parking(5, "CC..C", ".CC..") == 1
    assert occupy_parking(7, "CCCCCCC", "C.C.C.C") == 4
