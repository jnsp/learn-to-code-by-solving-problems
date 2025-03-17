# https://dmoj.ca/problem/coci08c1p2

from itertools import cycle


def winner(num_questions: int, answers: str) -> tuple[int, *tuple[str, ...]]:
    assert len(answers) == num_questions

    adrian = {"seq": cycle("ABC"), "score": 0, "name": "Adrian"}
    bruno = {"seq": cycle("BABC"), "score": 0, "name": "Bruno"}
    goran = {"seq": cycle("CCAABB"), "score": 0, "name": "Goran"}

    for a, b, g, answer in zip(adrian["seq"], bruno["seq"], goran["seq"], answers):
        if a == answer:
            adrian["score"] += 1
        if b == answer:
            bruno["score"] += 1
        if g == answer:
            goran["score"] += 1

    sorted_list = sorted([adrian, bruno, goran], key=lambda x: (-x["score"], x["name"]))
    max_score: int = sorted_list[0]["score"]
    max_scorers = [p["name"] for p in sorted_list if p["score"] == max_score]

    return max_score, *max_scorers


if __name__ == "__main__":
    num_questions = int(input())
    answers = input()
    max_score, *max_scorers = winner(num_questions, answers)

    print(max_score)
    for name in max_scorers:
        print(name)
