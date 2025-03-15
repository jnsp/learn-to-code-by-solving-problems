# https://dmoj.ca/problem/coci13c3p1


def display(n):
    a, b = 1, 0

    for _ in range(n):
        prev_a, prev_b = a, b
        a -= prev_a
        a += prev_b
        b += prev_a

    return a, b


if __name__ == "__main__":
    n = int(input())
    print(*display(n))
