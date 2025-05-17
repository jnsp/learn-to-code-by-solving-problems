# USACO 2017 February Contest, Bronze
# Problem 1. Why Did the Cow Cross the Road
# https://usaco.org/index.php?page=viewproblem2&cpid=711


def count_crossings(logs: list[tuple[int, int]]) -> int:
    crossings = 0
    locations = dict()

    for cow, location in logs:
        last_location = locations.get(cow)

        if last_location is not None and last_location != location:
            crossings += 1

        locations[cow] = location

    return crossings
