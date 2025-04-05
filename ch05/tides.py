# https://dmoj.ca/problem/dmopc14c7p2


def difference(tides: list[int]) -> int | str:
    min_tide = min(tides)
    max_tide = max(tides)
    diff = max_tide - min_tide

    index_min = tides.index(min_tide)
    index_max = tides.index(max_tide)

    if index_min >= index_max:
        return "unknown"

    min_to_max = tides[index_min : index_max + 1]
    is_increasing = all(previous < current for previous, current in zip(min_to_max, min_to_max[1:]))
    if not is_increasing:
        return "unknown"

    return diff


if __name__ == "__main__":
    n_tides = int(input())
    tides = [int(level) for level in input().split()]
    assert len(tides) == n_tides
    print(difference(tides))
