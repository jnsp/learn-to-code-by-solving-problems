# https://dmoj.ca/problem/ccc99s1


from itertools import cycle

HIGHS = {"ace": 4, "king": 3, "queen": 2, "jack": 1}


def no_high(deck: list[str]) -> bool:
    return all(card not in HIGHS for card in deck)


def play_game(deck: list[str]) -> tuple[list[tuple[str, int]], dict[str, int]]:
    reversed_deck = deck[::-1]
    point_logs = list()
    points = {"A": 0, "B": 0}
    players = cycle("AB")

    while reversed_deck:
        player = next(players)
        card = reversed_deck.pop()
        if card in HIGHS and len(reversed_deck) >= (point := HIGHS[card]) and no_high(reversed_deck[-point:]):
            point_logs.append((player, point))
            points[player] += point

    return point_logs, points


if __name__ == "__main__":
    NUM_CARDS = 52
    deck = [input() for _ in range(NUM_CARDS)]

    point_logs, points = play_game(deck)

    for player, point in point_logs:
        print(f"Player {player} scores {point} point(s).")

    for player, point in points.items():
        print(f"Player {player}: {point} point(s).")
