from tarifa import tarifa


def test_tarifa():
    assert tarifa(10, [4, 6, 2]) == 28
    assert tarifa(10, [10, 2, 12]) == 16
    assert tarifa(15, [15, 10, 20]) == 15
