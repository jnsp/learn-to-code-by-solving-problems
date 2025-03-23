# https://dmoj.ca/problem/ecoo13r1p1


def dispenser(taken_tickets: int, unsolved_tickets: int, next_number: int, action: str) -> tuple[int, int, int]:
    match action:
        case "TAKE":
            taken_tickets += 1
            unsolved_tickets += 1
            next_number += 1
            if next_number == 1000:
                next_number = 1
        case "SERVE":
            if unsolved_tickets > 0:
                unsolved_tickets -= 1
        case "CLOSE":
            pass
        case _:
            raise ValueError(f"Unknown action: {action}")

    return (taken_tickets, unsolved_tickets, next_number)


if __name__ == "__main__":
    taken_tickets = 0
    unsolved_tickets = 0
    next_number = int(input())

    while True:
        action = input()

        if action == "EOF":
            break

        taken_tickets, unsolved_tickets, next_number = dispenser(taken_tickets, unsolved_tickets, next_number, action)

        if action == "CLOSE":
            print(taken_tickets, unsolved_tickets, next_number)
            taken_tickets = 0
            unsolved_tickets = 0
