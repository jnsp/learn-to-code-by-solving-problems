# https://dmoj.ca/problem/ccc19j1


def winning_score(a3: int, a2: int, a1: int, b3: int, b2: int, b1: int) -> str:
    score_a = a3 * 3 + a2 * 2 + a1
    score_b = b3 * 3 + b2 * 2 + b1

    if score_a > score_b:
        return "A"
    elif score_b > score_a:
        return "B"
    else:
        return "T"


if __name__ == "__main__":
    a3 = int(input())
    a2 = int(input())
    a1 = int(input())
    b3 = int(input())
    b2 = int(input())
    b1 = int(input())
    print(winning_score(a3, a2, a1, b3, b2, b1))
