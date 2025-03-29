from baker_brie import Bakery


def test_insert_sales():
    bakery = Bakery()

    bakery.insert_sales([4, 3, 2, 4])
    assert bakery.sales[0] == [4, 3, 2, 4]

    bakery.insert_sales([3, 3, 2, 1])
    assert bakery.sales[1] == [3, 3, 2, 1]


def test_get_bonus():
    bakery = Bakery()
    sales = [
        [4, 3, 2, 4],
        [3, 3, 2, 1],
        [8, 2, 4, 1],
        [2, 2, 4, 3],
        [9, 3, 2, 3],
    ]

    for sale in sales:
        bakery.insert_sales(sale)

    assert bakery.get_bonus() == 4
