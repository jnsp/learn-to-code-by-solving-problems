# USACO 2013 December Contest, Bronze
# Problem 2. Cow Baseball
# https://usaco.org/index.php?page=viewproblem2&cpid=359


def max_points(swaps: list[tuple[int, int, int]]) -> float:
    max_points = float("-inf")
    pebbles = [
        [None, 1, 0, 0],
        [None, 0, 1, 0],
        [None, 0, 0, 1],
    ]

    for pebble in pebbles:
        points = 0
        for swap1, swap2, guess in swaps:
            pebble[swap1], pebble[swap2] = pebble[swap2], pebble[swap1]
            points += pebble[guess]

        max_points = max(max_points, points)

    return max_points
