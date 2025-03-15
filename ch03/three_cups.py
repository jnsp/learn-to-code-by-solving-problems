# https://dmoj.ca/problem/coci06c5p1


def three_cups2(swaps: str) -> int:
    ball_location = 1

    for swap in swaps:
        if swap == "A":
            if ball_location == 1:
                ball_location = 2
            elif ball_location == 2:
                ball_location = 1
        elif swap == "B":
            if ball_location == 2:
                ball_location = 3
            elif ball_location == 3:
                ball_location = 2
        elif swap == "C":
            if ball_location == 1:
                ball_location = 3
            elif ball_location == 3:
                ball_location = 1

    return ball_location


def three_cups(swaps: str) -> int:
    ball_location = 1

    swaps_paths = {("A", 1): 2, ("A", 2): 1, ("B", 2): 3, ("B", 3): 2, ("C", 1): 3, ("C", 3): 1}

    for swap in swaps:
        if (new_location := swaps_paths.get((swap, ball_location))) is not None:
            ball_location = new_location

    return ball_location


if __name__ == "__main__":
    swaps = input()
    print(three_cups(swaps))
