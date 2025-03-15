# https://dmoj.ca/problem/coci12c5p1


def decide_scale(composition: str) -> str:
    tones = composition.split("|")
    a_minor = {"A", "D", "E"}
    c_major = {"C", "F", "G"}

    a, c = 0, 0
    for tone in tones:
        if tone[0] in a_minor:
            a += 1
        elif tone[0] in c_major:
            c += 1

    if a > c:
        return "A-mol"
    elif c > a:
        return "C-dur"
    else:
        return "A-mol" if composition[-1] in a_minor else "C-dur"


if __name__ == "__main__":
    composition = input()
    print(decide_scale(composition))
