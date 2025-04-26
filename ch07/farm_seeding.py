# https://usaco.org/index.php?page=viewproblem2&cpid=916
# USACO 2019 February Contest, Bronze
# Problem 2. The Great Revegetation


def cows_with_favorite_pasture(favorites: dict[int, tuple[int, int]], pasture: int) -> set[int]:
    return {cow for cow, pastures in favorites.items() if pasture in pastures}


def types_used(favorites: dict[int, tuple[int, int]], cows: set[int], pasture_types: list[int]) -> set[int]:
    used = set()

    for cow in cows:
        pasture1, pasture2 = favorites[cow]
        if pasture1 < len(pasture_types):
            used.add(pasture_types[pasture1])
        if pasture2 < len(pasture_types):
            used.add(pasture_types[pasture2])

    return used


def smallest_available_type(eliminated: set[int]):
    pasture_type = 1
    while pasture_type in eliminated:
        pasture_type += 1
    return pasture_type


def main(n_pastures: int, favorites: dict[int, tuple[int, int]]):
    pasture_types = [0]

    for pasture in range(1, n_pastures + 1):
        cows = cows_with_favorite_pasture(favorites, pasture)
        eliminated = types_used(favorites, cows, pasture_types)
        pasture_type = smallest_available_type(eliminated)
        pasture_types.append(pasture_type)

    return pasture_types
