# https://dmoj.ca/problem/wac3p3


def points(moves: str, combos: dict[str, int]) -> int:
    points = len(moves)
    combos_to_search = sorted(combos.keys(), key=lambda x: len(x), reverse=True)
    n_moves = len(moves)
    index = 0

    while index <= n_moves:
        hit = False

        for combo in combos_to_search:
            if moves[index : index + len(combo)] == combo:
                hit = True
                points += combos[combo]
                index += len(combo)
                break

        if not hit:
            index += 1

    return points


if __name__ == "__main__":
    moves = input()
    n_combos = int(input())

    combos = dict()
    for _ in range(n_combos):
        combo, point = input().split()
        combos[combo] = int(point)

    print(points(moves, combos))
