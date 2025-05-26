# https://dmoj.ca/problem/coci14c2p2

from collections import Counter


def find_not_finished(registered: list[str], completed: list[str]) -> str:
    counter = Counter(registered)
    for athlete in completed:
        counter[athlete] -= 1

    for athlete, not_finished in counter.items():
        if not_finished:
            return athlete

    raise ValueError("No not finished athlete.")


if __name__ == "__main__":
    n = int(input())
    regisgered = [input() for _ in range(n)]
    completed = [input() for _ in range(n - 1)]

    not_finished = find_not_finished(regisgered, completed)
    print(not_finished)
