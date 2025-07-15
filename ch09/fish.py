# https://dmoj.ca/problem/ccc09j2

from itertools import product


def max_catches(points: tuple[int, ...], allowed: int) -> tuple[int, ...]:
    return tuple(allowed // p for p in points)


def catch_combination(points: tuple[int, ...], allowed: int) -> list[tuple[int, ...]]:
    brown_trout, northern_pike, yellow_pickerel = max_catches(points, allowed)
    combinations = product(range(brown_trout + 1), range(northern_pike + 1), range(yellow_pickerel + 1))

    results = list()
    for catches in combinations:
        total_points = sum(p * c for p, c in zip(points, catches))
        if 0 < total_points <= allowed:
            results.append(catches)
    return results


if __name__ == "__main__":
    *points, allowed = [int(input()) for _ in range(4)]
    results = catch_combination(tuple(points), allowed)
    for bt, np, yp in results:
        print(f"{bt} Brown Trout, {np} Northern Pike, {yp} Yellow Pickerel")
    print(f"Number of ways to catch fish: {len(results)}")
