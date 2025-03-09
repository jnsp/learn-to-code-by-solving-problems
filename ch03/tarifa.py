# https://dmoj.ca/problem/coci16c1p1


def tarifa(monthly: int, data: list[int]) -> int:
    extra = sum(monthly - d for d in data)
    return extra + monthly


if __name__ == "__main__":
    monthly = int(input())
    n_months = int(input())
    data = [int(input()) for _ in range(n_months)]
    print(tarifa(monthly, data))
