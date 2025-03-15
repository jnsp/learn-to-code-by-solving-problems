# https://dmoj.ca/problem/ccc00s1


def broke_when(quarters: int, slot_machine_played: tuple[int, int, int]) -> int:
    a_played, b_played, c_played = slot_machine_played
    n_spins = 0

    while quarters > 0:
        quarters -= 1
        n_spins += 1

        if n_spins % 3 == 1:
            a_played += 1
            if a_played % 35 == 0:
                quarters += 30
        elif n_spins % 3 == 2:
            b_played += 1
            if b_played % 100 == 0:
                quarters += 60
        else:
            c_played += 1
            if c_played % 10 == 0:
                quarters += 9

    return n_spins


if __name__ == "__main__":
    quarters = int(input())
    slot_machine_played = tuple(int(input()) for _ in range(3))
    assert len(slot_machine_played) == 3

    broke = broke_when(quarters, slot_machine_played)
    print(f"Martha plays {broke} times before going broke.")
