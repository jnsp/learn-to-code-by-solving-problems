from ptice import winner


def test_short_answers():
    num_questions = 5
    answers = "BAACC"
    assert winner(num_questions, answers) == (3, "Bruno")


def test_long_answers():
    num_questions = 9
    answers = "AAAABBBBB"
    assert winner(num_questions, answers) == (4, "Adrian", "Bruno", "Goran")
