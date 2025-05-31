# USACO 2014 January Contest, Bronze
# Problem 1. Ski Course Design
# https://usaco.org/index.php?page=viewproblem2&cpid=376

import math

MAX_DIFFERENCE = 17
MAX_HEIGHT = 100


def cost_for_range(heights: list[int]) -> float:
    min_cost = math.inf

    lowest = min(heights)
    highest = max(heights)

    if highest - MAX_DIFFERENCE >= lowest:
        upper_range = highest - MAX_DIFFERENCE
    else:
        upper_range = lowest + 17

    lows = range(lowest, upper_range + 1)
    for low in lows:
        high = low + MAX_DIFFERENCE

        cost = 0
        for height in heights:
            if height < low:
                cost += (low - height) ** 2
            if height > high:
                cost += (height - high) ** 2
        print(low, high)

        min_cost = cost if cost < min_cost else min_cost

    return min_cost
