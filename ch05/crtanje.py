# https://dmoj.ca/problem/coci20c2p1


def calculate_net_values(signs: str) -> list[int]:
    convert = {"+": 1, "-": -1, "=": 0}
    net_values = [0]
    for sign in signs:
        net_values.append(net_values[-1] + convert[sign])
    return net_values


def get_levels(net_values: list[int]) -> list[int]:
    min_net_value = min(net_values)
    clamped_net_values = [v - min_net_value for v in net_values]
    levels = []
    for current_value, next_value in zip(clamped_net_values, clamped_net_values[1:]):
        levels.append(min(current_value, next_value))
    return levels


def prepare_graph(levels: list[int]) -> list[list[str]]:
    n_days = len(levels)
    graph = [["."] * n_days for _ in set(levels)]
    return graph


def draw_graph(signs: str) -> list[list[str]]:
    net_values = calculate_net_values(signs)
    levels = get_levels(net_values)
    graph = prepare_graph(levels)

    for i, (sign, level) in enumerate(zip(signs, levels)):
        match sign:
            case "+":
                graph[level][i] = "/"
            case "-":
                graph[level][i] = "\\"
            case "=":
                graph[level][i] = "_"
            case _:
                raise ValueError(f"Unknown sign: {sign}.")

    graph.reverse()
    return graph


if __name__ == "__main__":
    n_days = int(input())
    signs = input()
    graph = draw_graph(signs)
    for line in graph:
        print("".join(line))
