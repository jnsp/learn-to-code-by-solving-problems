from multiple_choice import score


def test_score():
    responses = "ABC"
    answers = "ACB"
    assert score(responses, answers) == 1


def test_score2():
    responses = "AAA"
    answers = "ABA"
    assert score(responses, answers) == 2
