# https://dmoj.ca/problem/wc16c1j1


def spooky(n: int) -> str:
    return "sp" + "o" * n + "ky"


if __name__ == "__main__":
    n = int(input())
    print(spooky(n))
