from preokret import make_point_table, make_score_table, n_turnarounds, points_first_half


def test_make_point_table():
    times_point_a = [10, 1400, 1500]
    times_point_b = [7, 2000]
    expected_points_table = [
        [7, 0, 1],
        [10, 1, 0],
        [1400, 1, 0],
        [1500, 1, 0],
        [2000, 0, 1],
    ]

    assert make_point_table(times_point_a, times_point_b) == expected_points_table


def test_make_score_table():
    points_table = [
        [7, 0, 1],
        [10, 1, 0],
        [1400, 1, 0],
        [1500, 1, 0],
        [2000, 0, 1],
    ]
    expected_score_table = [
        [7, 0, 1, False],
        [10, 1, 1, False],
        [1400, 2, 1, True],
        [1500, 3, 1, False],
        [2000, 3, 2, False],
    ]

    assert make_score_table(points_table) == expected_score_table


def test_points_first_half():
    score_table = [
        [7, 0, 1, False],
        [10, 1, 1, False],
        [1400, 2, 1, True],
        [1500, 3, 1, False],
        [2000, 3, 2, False],
    ]

    assert points_first_half(score_table) == 3


def test_turnarounds():
    score_table = [
        [7, 0, 1, False],
        [10, 1, 1, False],
        [1400, 2, 1, True],
        [1500, 3, 1, False],
        [2000, 3, 2, False],
    ]

    assert n_turnarounds(score_table) == 1
