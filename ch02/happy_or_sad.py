# https://dmoj.ca/problem/ccc15j2


def happy_or_sad(text: str) -> str:
    happy = text.count(":-)")
    sad = text.count(":-(")

    if happy == 0 and sad == 0:
        return "none"
    elif happy == sad:
        return "unsure"
    elif happy > sad:
        return "happy"
    else:
        return "sad"


if __name__ == "__main__":
    text = input()
    print(happy_or_sad(text))
