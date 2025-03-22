# https://dmoj.ca/problem/ccc00s1


def which_machine(n_spins: int) -> str:
    machine_indicator = n_spins % 3
    match machine_indicator:
        case 1:
            machine = "a"
        case 2:
            machine = "b"
        case 0:
            machine = "c"
        case _:
            raise ValueError("There is no slotmachine.")
    return machine


def broke_when(quarters: int, slot_machine_played: tuple[int, int, int]) -> int:
    a_played, b_played, c_played = slot_machine_played
    n_spins = 0

    while quarters > 0:
        quarters -= 1
        n_spins += 1

        machine = which_machine(n_spins)
        if machine == "a":
            a_played += 1
            if a_played % 35 == 0:
                quarters += 30
        elif machine == "b":
            b_played += 1
            if b_played % 100 == 0:
                quarters += 60
        elif machine == "c":
            c_played += 1
            if c_played % 10 == 0:
                quarters += 9
        else:
            raise ValueError("There is no slotmachine.")

    return n_spins


if __name__ == "__main__":
    quarters = int(input())
    slot_machine_played = tuple(int(input()) for _ in range(3))
    assert len(slot_machine_played) == 3

    broke = broke_when(quarters, slot_machine_played)
    print(f"Martha plays {broke} times before going broke.")
