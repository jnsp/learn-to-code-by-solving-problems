# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector

from bisect import bisect_right


def max_diamonds(sizes: list[int], k: int) -> float:
    max_value = float("-inf")
    sizes.sort()

    for i, size in enumerate(sizes):
        high = size + k
        right = bisect_right(sizes, high)
        number_of_diamonds = right - i
        max_value = max(number_of_diamonds, max_value)

    return max_value
