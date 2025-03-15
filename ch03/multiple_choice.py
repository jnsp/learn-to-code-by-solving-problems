# https://dmoj.ca/problem/ccc11s2


def score(responses, answers):
    return sum(r == a for r, a in zip(responses, answers))


if __name__ == "__main__":
    n_questions = int(input())

    responses = ""
    for _ in range(n_questions):
        responses += input()

    answers = ""
    for _ in range(n_questions):
        answers += input()

    print(score(responses, answers))
