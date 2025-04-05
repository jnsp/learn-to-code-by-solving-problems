# https://dmoj.ca/problem/coci19c5p1


def count_rectangles(rectangles: list[str]) -> int:
    n_rectagles = 0
    edge = ".*"
    len_line = len(rectangles[0])
    previous_padded_line = "." * (len_line + 1)

    for line in rectangles:
        padded_line = "." + line

        for index in range(len_line):
            searching_block = padded_line[index : index + 2]
            previous_searching_block = previous_padded_line[index : index + 2]

            if searching_block == edge and previous_searching_block != edge:
                n_rectagles += 1

        previous_padded_line = padded_line

    return n_rectagles


if __name__ == "__main__":
    n_line, _ = [int(v) for v in input().split()]
    rectangles = []
    for _ in range(n_line):
        rectangles.append(input())

    print(count_rectangles(rectangles))
