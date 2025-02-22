# https://dmoj.ca/problem/dmopc14c5p1

import math


def cone_volume(radius, height):
    return (1 / 3) * math.pi * radius**2 * height


if __name__ == "__main__":
    r = int(input())
    h = int(input())
    print(cone_volume(r, h))
