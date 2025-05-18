# USACO 2019 December Contest, Bronze
# Problem 1. Cow Gymnastics
# https://usaco.org/index.php?page=viewproblem2&cpid=963

from collections.abc import Iterable
from itertools import combinations


def pairs(n_cows: int) -> Iterable:
    return combinations(range(1, n_cows + 1), 2)


def is_better(pair: tuple[int, int], record: tuple[int, ...]) -> bool:
    a, b = pair
    rank_a = record.index(a)
    rank_b = record.index(b)
    return rank_a < rank_b


def count_consistent(n_cows: int, records: list[tuple[int, ...]]) -> int:
    n_consistent = 0

    for pair in pairs(n_cows):
        comparisons = [is_better(pair, record) for record in records]

        if len(set(comparisons)) == 1:
            n_consistent += 1

    return n_consistent
