# https://dmoj.ca/problem/coci08c3p2


def decode(encoded: str) -> str:
    decoded = ""
    i = 0
    while i < len(encoded):
        decoded += encoded[i]
        if encoded[i] in "aeiou":
            i += 3
        else:
            i += 1

    return decoded


if __name__ == "__main__":
    encoded = input()
    print(decode(encoded))
