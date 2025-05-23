# USACO 2016 December Contest, Silver
# Problem 2. Cities and States
# https://usaco.org/index.php?page=viewproblem2&cpid=667

from collections import defaultdict


def count_pairs(cities_and_states: list[str]) -> int:
    abbres = defaultdict(int)
    for value in cities_and_states:
        city, state = value.split()
        if (city := city[:2]) != state:
            abbreviation = city + state
            abbres[abbreviation] += 1

    total = 0
    for abbre in abbres:
        inverted = abbre[2:] + abbre[:2]
        total += abbres[abbre] * abbres.get(inverted, 0)

    return int(total / 2)
