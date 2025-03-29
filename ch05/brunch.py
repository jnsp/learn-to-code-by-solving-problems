# https://dmoj.ca/problem/ecoo17r1p1


def enough_fund(cost_trip: int, percentages_grade: list[float], n_students: int) -> bool:
    prices = [12, 10, 7, 5]

    n_grades = [int(n_students * pert) for pert in percentages_grade]
    uncounted = n_students - sum(n_grades)
    n_grades[percentages_grade.index(max(percentages_grade))] += uncounted

    revenue = sum(price * n_grade for price, n_grade in zip(prices, n_grades))

    return revenue * 0.5 >= cost_trip


if __name__ == "__main__":
    for _ in range(10):
        cost_trip = int(input())
        percentages_grade = input()
        percentages_grade = [float(p) for p in percentages_grade.split()]
        n_students = int(input())

        is_enough = enough_fund(cost_trip, percentages_grade, n_students)
        need_more_funds = "NO" if is_enough else "YES"

        print(need_more_funds)
