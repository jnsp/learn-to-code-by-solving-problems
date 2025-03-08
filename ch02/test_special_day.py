from special_day import special_day, special_day2


def test_special_day():
    assert special_day(2, 18) == "Special"
    assert special_day(2, 17) == "Before"
    assert special_day(2, 19) == "After"
    assert special_day(1, 7) == "Before"
    assert special_day(8, 31) == "After"


def test_special_day2():
    assert special_day2(2, 18) == "Special"
    assert special_day2(2, 17) == "Before"
    assert special_day2(2, 19) == "After"
    assert special_day2(1, 7) == "Before"
    assert special_day2(8, 31) == "After"
