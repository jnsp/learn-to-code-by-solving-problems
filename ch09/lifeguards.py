# USACO 2018 January Contest, Bronze
# Problem 2. Lifeguards
# https://usaco.org/index.php?page=viewproblem2&cpid=784


def covered_if_fired(intervals: list[tuple[int, int]], fired: int) -> int:
    covered = set()
    for i, (start, end) in enumerate(intervals):
        if i == fired:
            continue
        for time in range(start, end):
            covered.add(time)
    return len(covered)


def covered(intervals: list[tuple[int, int]]) -> int:
    max_number = 0
    for fired in range(len(intervals)):
        number = covered_if_fired(intervals, fired)
        if number > max_number:
            max_number = number

    return max_number
