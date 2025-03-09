# https://dmoj.ca/problem/ccc07j1


# Don't use sorted() or max() or min()
def middle(a: int, b: int, c: int) -> int:
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    else:
        return c


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(middle(a, b, c))
