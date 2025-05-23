# https://dmoj.ca/problem/cco99p2

from collections import Counter, defaultdict


def invert_counter(counter: Counter) -> dict[int, list[str]]:
    result = defaultdict(list)
    for word, count in counter.most_common():
        result[count].append(word)
    return result


def get_kth_most_common_words(inverted_counter: dict[int, list[str]], k: int) -> list[str] | None:
    all_counts = 0
    for _, words in inverted_counter.items():
        if k - 1 == all_counts:
            return words
        all_counts += len(words)


def common_words(words: list[str], k: int) -> list[str] | None:
    c = Counter(words)
    inverted = invert_counter(c)
    return get_kth_most_common_words(inverted, k)


def kth_notation(k: int) -> str:
    ten_digit = k % 10
    hundred_digit = k % 100

    if ten_digit == 1 and not (11 <= hundred_digit <= 13):
        suffix = "st"
    elif ten_digit == 2 and not (11 <= hundred_digit <= 13):
        suffix = "nd"
    elif ten_digit == 3 and not (11 <= hundred_digit <= 13):
        suffix = "rd"
    else:
        suffix = "th"

    return str(k) + suffix


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        n_words, k = [int(i) for i in input().split()]
        words = [input() for _ in range(n_words)]
        result = common_words(words, k)

        notation = kth_notation(k)
        print(f"{notation} most common word(s):")
        if result is not None:
            for word in result:
                print(word)

        print("\n")
