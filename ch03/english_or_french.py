# https://dmoj.ca/problem/ccc11s1


def detect_lang(text):
    text = text.lower()
    count_s = text.count("s")
    count_t = text.count("t")

    return "English" if count_t > count_s else "French"


if __name__ == "__main__":
    text = ""
    n_line = int(input())
    for _ in range(n_line):
        text += input()

    print(detect_lang(text))
