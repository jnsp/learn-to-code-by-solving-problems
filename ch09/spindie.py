# https://dmoj.ca/problem/ecoo16r1p2

from itertools import combinations_with_replacement


def is_possible(spinners: list[int], targets: list[int]) -> str:
    unique_spinners = set(spinners)
    intermediates = set()

    for s1, s2 in combinations_with_replacement(unique_spinners, 2):
        intermediates.add(s1 + s2)
        intermediates.add(s1 * s2)

    result = ""
    for target in targets:
        hit = False

        for s3 in unique_spinners:
            if target / s3 in intermediates or target - s3 in intermediates:
                hit = True
                break

        result += "T" if hit else "F"

    return result


if __name__ == "__main__":
    for _ in range(10):
        n_integers = int(input())
        spinners = [int(integer) for integer in input().split()]
        assert len(spinners) == n_integers
        targets = [int(target) for target in input().split()]
        result = is_possible(spinners, targets)
        print(result)
