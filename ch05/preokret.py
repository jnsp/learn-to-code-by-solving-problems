# https://dmoj.ca/problem/coci18c2p1


def make_point_table(times_point_a: list[int], times_point_b: list[int]) -> list[list[int]]:
    points_a = [[t, 1, 0] for t in times_point_a]
    points_b = [[t, 0, 1] for t in times_point_b]
    points = sorted(points_a + points_b)
    return points


def make_score_table(points_table: list[list[int]]) -> list[list]:
    scores = []
    score_a = 0
    score_b = 0
    previous_winning = "A" if points_table[0][1] > points_table[0][2] else "B"

    for point_log in points_table:
        turnaround = False
        score_a += point_log[1]
        score_b += point_log[2]

        if score_a > score_b:
            winning = "A"
        elif score_a < score_b:
            winning = "B"
        else:
            winning = previous_winning

        turnaround = previous_winning != winning
        previous_winning = winning

        scores.append([point_log[0], score_a, score_b, turnaround])

    return scores


def points_first_half(scores: list[list]) -> int:
    points = max([t, a, b] for t, a, b, _ in scores if t <= 1440)
    return sum(points[1:])


def n_turnarounds(scores: list[list]) -> int:
    return sum(t for *_, t in scores)


if __name__ == "__main__":
    n_points_a = int(input())
    points_a = [int(input()) for _ in range(n_points_a)]
    n_points_b = int(input())
    points_b = [int(input()) for _ in range(n_points_b)]

    points_table = make_point_table(points_a, points_b)
    score_table = make_score_table(points_table)

    print(points_first_half(score_table))
    print(n_turnarounds(score_table))
