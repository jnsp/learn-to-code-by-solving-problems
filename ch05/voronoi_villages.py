# https://dmoj.ca/problem/ccc18s1


def smallest_size(locations: list[int]) -> float:
    sorted_locations = sorted(locations)
    sizes = []

    for i in range(1, len(sorted_locations) - 1):
        left_size = (sorted_locations[i] - sorted_locations[i - 1]) / 2
        right_size = (sorted_locations[i + 1] - sorted_locations[i]) / 2
        sizes.append(left_size + right_size)

    return min(sizes)


if __name__ == "__main__":
    n = int(input())
    locations = [int(input()) for _ in range(n)]
    print(smallest_size(locations))
