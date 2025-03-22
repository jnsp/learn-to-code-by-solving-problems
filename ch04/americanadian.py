# https://dmoj.ca/problem/ccc02j2


def translate(word: str) -> str:
    if len(word) > 4 and word[-2:] == "or" and word[-3] not in "aeiouy":
        word = word.replace("or", "our")

    return word


if __name__ == "__main__":
    while True:
        word = input()
        if word == "quit!":
            break
        print(translate(word))
