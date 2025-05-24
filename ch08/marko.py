# https://dmoj.ca/problem/coci15c2p1

KEY_MAP = {
    2: {"a", "b", "c"},
    3: {"d", "e", "f"},
    4: {"g", "h", "i"},
    5: {"j", "k", "l"},
    6: {"m", "n", "o"},
    7: {"p", "q", "r", "s"},
    8: {"t", "u", "v"},
    9: {"w", "x", "y", "z"},
}


def count_mappable_words(words: list[str], keys_pressed: str) -> int:
    count = 0
    n_pressed = len(keys_pressed)

    for word in words:
        if len(word) != n_pressed:
            continue

        if all(letter in KEY_MAP[int(key)] for letter, key in zip(word, keys_pressed)):
            count += 1

    return count


def get_data() -> tuple[list[str], str]:
    n_words = int(input())
    words = [input() for _ in range(n_words)]
    keys_pressed = input()
    return words, keys_pressed


if __name__ == "__main__":
    words, keys_pressed = get_data()
    print(count_mappable_words(words, keys_pressed))
