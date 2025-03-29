from brunch import enough_fund


def test_enough_fund1():
    cost_trip = 4000
    percentages_grade = [0.5, 0.2, 0.1, 0.2]
    n_students = 400

    assert enough_fund(cost_trip, percentages_grade, n_students) is False


def test_enough_fund2():
    cost_trip = 6000
    percentages_grade = [0.1, 0.1, 0.45, 0.35]
    n_students = 2000

    assert enough_fund(cost_trip, percentages_grade, n_students) is True
