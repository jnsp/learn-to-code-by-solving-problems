# https://dmoj.ca/problem/ccc07j3


def expected_value(numbers: list[int]) -> float:
    briefcases = {
        1: 100,
        2: 500,
        3: 1_000,
        4: 5_000,
        5: 10_000,
        6: 25_000,
        7: 50_000,
        8: 100_000,
        9: 500_000,
        10: 1_000_000,
    }

    expected_value = sum(v for k, v in briefcases.items() if k not in numbers) / (10 - len(numbers))
    return expected_value


if __name__ == "__main__":
    n_opened_cases = int(input())
    opened_cases = [int(input()) for _ in range(n_opened_cases)]
    offered_value = int(input())
    expected = expected_value(opened_cases)

    if offered_value > expected:
        print("deal")
    else:
        print("no deal")
