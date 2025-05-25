# https://dmoj.ca/problem/dmopc19c3p1

from collections import Counter


def find_modes(values: list[int]) -> list[int]:
    c = Counter(values)
    most_common = c.most_common()
    _, highest_frequency = most_common[0]

    modes = []
    for value, frequency in most_common:
        if frequency != highest_frequency:
            break
        modes.append(value)

    return sorted(modes)


if __name__ == "__main__":
    n = int(input())
    values = [int(v) for v in input().split()]
    assert len(values) == n

    modes = find_modes(values)
    print(" ".join(str(v) for v in modes))
