# https://dmoj.ca/problem/ccc00s2


def split(streams: list[int], to_split: int, percentage_to_left: int) -> list[int]:
    to_split -= 1

    left_stream = round(streams[to_split] * (percentage_to_left / 100))
    right_stream = streams[to_split] - left_stream
    split_streams = [left_stream, right_stream]

    new_streams = streams[:to_split] + split_streams + streams[to_split + 1 :]
    return new_streams


def join(streams: list[int], to_join: int) -> list[int]:
    to_join -= 1

    joined_stream = streams[to_join] + streams[to_join + 1]

    new_streams = streams[:to_join] + [joined_stream] + streams[to_join + 2 :]
    return new_streams


if __name__ == "__main__":
    n_streams = int(input())
    streams = [int(input()) for _ in range(n_streams)]
    actions = {99: "SPLIT", 88: "JOIN", 77: "END"}

    while True:
        action = actions[int(input())]

        match action:
            case "SPLIT":
                to_split = int(input())
                percentage_to_left = int(input())
                streams = split(streams, to_split, percentage_to_left)
            case "JOIN":
                to_join = int(input())
                streams = join(streams, to_join)
            case "END":
                print(*streams)
                break
