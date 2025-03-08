# https://dmoj.ca/problem/ccc18j1


def telemarketer(a: int, b: int, c: int, d: int) -> str:
    condition_1 = a == 8 or a == 9
    condition_2 = d == 8 or d == 9
    condition_3 = b == c

    if condition_1 and condition_2 and condition_3:
        return "ignore"
    else:
        return "answer"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(telemarketer(a, b, c, d))
