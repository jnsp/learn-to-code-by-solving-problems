# https://dmoj.ca/problem/wac3p3


def hit_combo(moves: str, combo: str) -> tuple[bool, str]:
    if not combo:
        return False, moves

    return combo in moves, moves.replace(combo, "*", 1)


def sort_combos(moves: str, combos: list[str]) -> list[str]:
    combos_priority = [(combo, moves.find(combo), -len(combo)) for combo in combos if combo in moves]
    sorted_combos = sorted(combos_priority, key=lambda x: x[1:], reverse=True)
    return [combo for combo, *_ in sorted_combos]


def points(moves: str, combos: dict[str, int]) -> int:
    points = len(moves)
    combos_to_search = list(combos.keys())

    while combos_to_search:
        if not (combos_to_search := sort_combos(moves, combos_to_search)):
            break

        combo = combos_to_search.pop()
        hit, moves = hit_combo(moves, combo)
        points += combos[combo] * hit

        if combo in moves:
            combos_to_search.append(combo)

    return points


if __name__ == "__main__":
    moves = input()
    n_combos = int(input())

    combos = dict()
    for _ in range(n_combos):
        combo, point = input().split()
        combos[combo] = int(point)

    print(points(moves, combos))
