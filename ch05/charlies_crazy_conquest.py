# https://dmoj.ca/problem/dmopc19c5p2


def make_logs(logs_a: list[tuple[str, int]], logs_b: list[tuple[str, int]]) -> list[tuple[str, int]]:
    actions = list()
    for action_a, action_b in zip(logs_a, logs_b):
        actions.append(action_a)
        actions.append(action_b)
    return actions


def simulate(health: int, logs_a: list[tuple[str, int]], logs_b: list[tuple[str, int]]) -> str:
    healths = {"A": health, "B": health}
    logs = make_logs(logs_a, logs_b)
    previous_logs = [("START", 0)] + logs
    current_logs = logs + [("END", 0)]

    for i, (previous_log, current_log) in enumerate(zip(previous_logs, current_logs)):
        turn = "A" if i % 2 == 0 else "B"
        opponent = "B" if turn == "A" else "A"

        previous_action, previous_damage = previous_log
        current_action, current_damage = current_log

        match previous_action, current_action:
            case "A" | "START", "A":
                healths[opponent] -= current_damage
            case "D", "D" | "END":
                healths[opponent] -= previous_damage
            case _:
                pass

        if healths["A"] <= 0:
            return "DEFEAT"

        if healths["B"] <= 0:
            return "VICTORY"

    return "TIE"


if __name__ == "__main__":
    n_logs, health = [int(value) for value in input().split()]

    collection_logs = list()
    for _ in range(2):
        logs = list()

        for _ in range(n_logs):
            action, damage = input().split()
            logs.append((action, int(damage)))

        collection_logs.append(logs)

    print(simulate(health, *collection_logs))
