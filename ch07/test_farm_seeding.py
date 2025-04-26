from farm_seeding import cows_with_favorite_pasture, main, smallest_available_type, types_used


def test_cows_withfavorite_pasture():
    favorites = {
        # cow: (pasture, pasture)
        1: (5, 4),
        2: (2, 4),
        3: (3, 5),
        4: (4, 1),
        5: (2, 1),
        6: (5, 2),
    }

    assert cows_with_favorite_pasture(favorites, 1) == {4, 5}
    assert cows_with_favorite_pasture(favorites, 2) == {2, 5, 6}
    assert cows_with_favorite_pasture(favorites, 3) == {3}


def test_types_used():
    favorites = {
        # cow: (pasture, pasture)
        1: (5, 4),
        2: (2, 4),
        3: (3, 5),
        4: (4, 1),
        5: (2, 1),
        6: (5, 2),
    }

    pasture_types = [0]
    assert types_used(favorites, {4, 5}, pasture_types) == set()

    pasture_types = [0, 1]
    assert types_used(favorites, {4, 5}, pasture_types) == {1}


def test_smallest_available_type():
    eliminated = {1}
    assert smallest_available_type(eliminated) == 2


def test_main():
    n_pastures = 8
    favotrites = {
        # cow: (pasture, pasture)
        1: (5, 4),
        2: (2, 4),
        3: (3, 5),
        4: (4, 1),
        5: (2, 1),
        6: (5, 2),
    }
    assert main(n_pastures, favotrites) == [0, 1, 2, 1, 3, 4, 1, 1, 1]
