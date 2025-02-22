# https://dmoj.ca/problem/wc15c2j1


def new_hope(n: int) -> str:
    return "A long time ago in a galaxy " + "far, " * (n - 1) + "far " * (n >= 1) + "away..."


if __name__ == "__main__":
    n = int(input())
    print(new_hope(n))
