# https://dmoj.ca/problem/dmopc19c5p1


def complete_assignments(items: set[str], assignments: list[list[str]]) -> int:
    completed = 0

    for assignment in assignments:
        if items >= set(assignment):
            completed += 1

    return completed


def get_items_and_assignments() -> tuple[set[str], list[list[str]]]:
    n_items, n_assignments = [int(v) for v in input().split()]

    items = {input() for _ in range(n_items)}

    assignments = []
    for _ in range(n_assignments):
        n_assignment = int(input())
        assignment = [input() for _ in range(n_assignment)]
        assignments.append(assignment)

    return items, assignments


if __name__ == "__main__":
    items, assignments = get_items_and_assignments()
    print(complete_assignments(items, assignments))
