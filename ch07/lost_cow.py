# USACO 2017 US Open Contest, Bronze
# Problem 1. The Lost Cow
# https://usaco.org/index.php?page=viewproblem2&cpid=735


def travel(farmer: int, cow: int) -> int:
    total_travel = 0
    current_position = farmer
    search_distance = 1

    while True:
        next_position = farmer + search_distance

        if (current_position <= cow <= next_position) or (next_position <= cow <= current_position):
            total_travel += abs(cow - current_position)
            return total_travel

        total_travel += abs(next_position - current_position)

        current_position = next_position
        search_distance *= -2
