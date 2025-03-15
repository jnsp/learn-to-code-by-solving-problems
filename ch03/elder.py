# https://dmoj.ca/problem/coci18c4p1


def obey_who(original_wizard: str, duels: list[tuple[str, str]]) -> tuple[str, int]:
    already_obeyed = set(original_wizard)
    wiazrd_with_wand = original_wizard

    for duel in duels:
        winner, loser = duel
        if loser == wiazrd_with_wand:
            wiazrd_with_wand = winner
            already_obeyed.add(winner)

    return wiazrd_with_wand, len(already_obeyed)


if __name__ == "__main__":
    original_wizard = input()
    n_duels = int(input())

    duels = [tuple(input().split()) for _ in range(n_duels)]

    wizard, n_wizard_obeyed = obey_who(original_wizard, duels)
    print(wizard)
    print(n_wizard_obeyed)
