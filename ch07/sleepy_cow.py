# USACO 2019 February Contest, Bronze
# Problem 1. Sleepy Cow Herding
# https://usaco.org/index.php?page=viewproblem2&cpid=915


def count_moves(locations: tuple[int, int, int]) -> tuple[int, int]:
    d1 = locations[1] - locations[0]
    d2 = locations[2] - locations[1]
    ds = [d1, d2]

    if d1 == d2 == 1:
        return 0, 0

    if 2 in ds:
        min_move = 1
    else:
        min_move = 2

    max_move = max(ds) - 1

    return min_move, max_move
