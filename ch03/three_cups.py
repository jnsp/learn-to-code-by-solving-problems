# https://dmoj.ca/problem/coci06c5p1


def three_cups(swaps: str) -> int:
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


if __name__ == "__main__":
    swaps = input()
    print(three_cups(swaps))
