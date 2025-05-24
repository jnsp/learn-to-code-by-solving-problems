# https://dmoj.ca/problem/crci06p1

from collections import defaultdict


def villagers_with_all_songs(evenings: list[list[int]]) -> list[int]:
    villagers_songs = defaultdict(set)
    bard = 1

    for i, villagers in enumerate(evenings):
        if bard in villagers:
            for villager in villagers:
                villagers_songs[villager].add(f"song#{i}")
        else:
            exchanged_songs = set()
            for villager in villagers:
                exchanged_songs |= villagers_songs[villager]
            for villager in villagers:
                villagers_songs[villager] |= exchanged_songs

    all_songs = villagers_songs[bard]
    result = [villager for villager, songs in villagers_songs.items() if songs == all_songs]

    return sorted(result)


def get_evenings() -> list[list[int]]:
    _ = int(input())
    n_evenings = int(input())

    evenings = []
    for _ in range(n_evenings):
        evening = [int(v) for v in input().split()][1:]
        evenings.append(evening)

    return evenings


if __name__ == "__main__":
    evenings = get_evenings()
    villagers = villagers_with_all_songs(evenings)
    for villager in villagers:
        print(villager)
