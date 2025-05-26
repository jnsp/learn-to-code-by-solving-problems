# https://dmoj.ca/problem/coci17c2p2

from collections import defaultdict
from itertools import cycle


def answered_words(words: list[str], asked: str) -> list[str]:
    dictionary = defaultdict(list)
    for word in words:
        first_letter = word[0]
        dictionary[first_letter].append(word)

    cyclers = {}
    for first_letter, words in dictionary.items():
        cyclers[first_letter] = cycle(sorted(words))

    return [next(cyclers[first_letter]) for first_letter in asked]


if __name__ == "__main__":
    n_words, n_letters = [int(v) for v in input().split()]
    words = [input() for _ in range(n_words)]
    asked = "".join(input() for _ in range(n_letters))

    result = answered_words(words, asked)
    for word in result:
        print(word)
