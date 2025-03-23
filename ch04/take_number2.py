# https://dmoj.ca/problem/ecoo13r1p1


class Dispenser:
    def __init__(self, next_number: int = 0):
        self.taken_tickets = 0
        self.unsolved_tickets = 0
        self.next_number = next_number

    def take(self):
        self.taken_tickets += 1
        self.unsolved_tickets += 1
        self.next_number += 1

        if self.next_number == 1000:
            self.next_number = 1

    def serve(self):
        if self.unsolved_tickets > 0:
            self.unsolved_tickets -= 1

    def close(self) -> tuple[int, int, int]:
        taken_tickets = self.taken_tickets
        unsolved_tickets = self.unsolved_tickets

        self.taken_tickets = 0
        self.unsolved_tickets = 0

        return taken_tickets, unsolved_tickets, self.next_number


if __name__ == "__main__":
    next_number = int(input())
    dispenser = Dispenser(next_number)

    while True:
        action = input()

        match action:
            case "TAKE":
                dispenser.take()
            case "SERVE":
                dispenser.serve()
            case "CLOSE":
                print(*dispenser.close())
            case "EOF":
                break
