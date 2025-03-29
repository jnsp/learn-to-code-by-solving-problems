# https://dmoj.ca/problem/coci17c1p1


def numbers_cards(drawn_cards: list[int]) -> tuple[int, int]:
    cards = {rank: 4 for rank in range(2, 12)}
    cards[10] += 12

    for drawn_card in drawn_cards:
        cards[drawn_card] -= 1

    buffer = 21 - sum(drawn_cards)

    numbers_higher_cards, numbers_lower_cards = 0, 0

    for rank, n in cards.items():
        if rank > buffer:
            numbers_higher_cards += n
        else:
            numbers_lower_cards += n

    return numbers_higher_cards, numbers_lower_cards


if __name__ == "__main__":
    n_drawn = int(input())
    drawn_cards = []
    for _ in range(n_drawn):
        drawn_cards.append(int(input()))

    higher, lower = numbers_cards(drawn_cards)

    if higher >= lower:
        print("DOSTA")
    else:
        print("VUCI")
