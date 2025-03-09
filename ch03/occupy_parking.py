# https://dmoj.ca/problem/ccc18j2


def occupy_parking(n_slots: int, yesterday: str, today: str) -> int:
    assert len(yesterday) == len(today) == n_slots

    count = 0
    for y, t in zip(yesterday, today):
        if y == t == "C":
            count += 1

    return count


if __name__ == "__main__":
    n_slots = int(input())
    yesterday = input()
    today = input()
    print(occupy_parking(n_slots, yesterday, today))
