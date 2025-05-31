# USACO 2013 December Contest, Bronze
# Problem 2. Cow Baseball
# https://usaco.org/index.php?page=viewproblem2&cpid=359

from bisect import bisect_left, bisect_right


def count_triples(positions: list[int]) -> int:
    positions.sort()
    n_triples = 0
    n_positions = len(positions)

    for i in range(n_positions - 2):
        for j in range(i + 1, n_positions - 1):
            distance = positions[j] - positions[i]

            low = positions[j] + distance
            high = positions[j] + distance * 2

            left = bisect_left(positions, low)
            right = bisect_right(positions, high)

            n_triples += right - left

    return n_triples
