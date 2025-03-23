# https://dmoj.ca/problem/ccc19j3


def encode(string) -> list[tuple[str, int]]:
    string += "\n"
    current_char = string[0]
    count = 0

    result = []
    for char in string:
        if current_char == char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    return result


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        string = input()
        encoded = encode(string)

        result = ""
        for i, (char, n) in enumerate(encoded):
            result += str(n) + " " + char + ("" if i == len(encoded) else " ")
        print(result)
