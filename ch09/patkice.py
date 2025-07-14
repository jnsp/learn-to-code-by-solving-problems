# https://dmoj.ca/problem/coci20c1p1


def find_start(map: list[str]) -> list[int]:
    for i, row in enumerate(map):
        for j, position in enumerate(row):
            if position == "o":
                return [i, j]

    raise ValueError("There is no start point.")


def move(current_position: list[int], direction: str) -> list[int]:
    match direction:
        case "N" | "^":
            new_position = [current_position[0] - 1, current_position[1]]
        case "E" | ">":
            new_position = [current_position[0], current_position[1] + 1]
        case "W" | "<":
            new_position = [current_position[0], current_position[1] - 1]
        case "S" | "v":
            new_position = [current_position[0] + 1, current_position[1]]
        case _:
            raise ValueError("Invalid direction")

    return new_position


def voyage(map: list[str]) -> tuple[str, ...]:
    start_position = find_start(map)
    results = list()

    for direction in "NEWS":
        position = move(start_position, direction)

        n = 0
        while (cell := map[position[0]][position[1]]) not in "o.":
            if cell == "x":
                results.append((n, direction))
                break
            else:
                position = move(position, cell)
                n += 1

    if len(results) > 0:
        best_direction = min(results)[1]
        return ":)", best_direction
    else:
        return (":(",)


if __name__ == "__main__":
    r, _ = [int(v) for v in input().split()]
    map = [input() for _ in range(r)]

    result = voyage(map)
    for item in result:
        print(item)
