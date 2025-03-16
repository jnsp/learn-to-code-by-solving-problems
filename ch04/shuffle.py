# https://dmoj.ca/problem/ccc08j2


def move_first_to_end(songs: list[str]) -> list[str]:
    return songs[1:] + [songs[0]]


def move_last_to_start(songs: list[str]) -> list[str]:
    return [songs[-1]] + songs[:-1]


def swap_first_and_second(songs: list[str]) -> list[str]:
    return [songs[1], songs[0]] + songs[2:]


def shuffle(songs: list[str], actions: list[tuple[int, int]]) -> list[str]:
    for action, n_repeat in actions:
        if action == 1:
            for _ in range(n_repeat):
                songs = move_first_to_end(songs)
        elif action == 2:
            for _ in range(n_repeat):
                songs = move_last_to_start(songs)
        elif action == 3:
            for _ in range(n_repeat):
                songs = swap_first_and_second(songs)
        elif action == 4:
            break
        else:
            raise ValueError(f"Unknown action {action}")

    return songs


if __name__ == "__main__":
    songs = ["A", "B", "C", "D", "E"]
    action = None
    actions = []
    while action != 4:
        action = int(input())
        n_repeat = int(input())
        actions.append((action, n_repeat))

    print(*shuffle(songs, actions))
