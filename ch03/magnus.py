# https://dmoj.ca/problem/coci18c3p1
from itertools import cycle


def honi(string):
    search = "HONI"
    search_cycle = cycle(search)
    result = ""

    char_search = next(search_cycle)
    for char in string:
        if char == char_search:
            result += char
            char_search = next(search_cycle)

    return result.count(search)


if __name__ == "__main__":
    s = input()
    print(honi(s))
