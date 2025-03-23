# https://dmoj.ca/problem/ecoo15r1p1

import math


def gather_smarties(container: dict[str, int], smarty: str):
    container[smarty] += 1


def calculate_time(container: dict[str, int]) -> int:
    time = 0
    for color, n in container.items():
        if color == "red":
            time += n * 16
        else:
            time += math.ceil(n / 7) * 13
    return time


if __name__ == "__main__":
    for _ in range(10):
        container = {"orange": 0, "blue": 0, "green": 0, "yellow": 0, "pink": 0, "violet": 0, "brown": 0, "red": 0}
        while True:
            info = input()
            if info == "end of box":
                print(calculate_time(container))
                break
            else:
                gather_smarties(container, info)
