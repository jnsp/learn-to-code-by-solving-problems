from telemarketer import telemarketer


def test_ignore():
    assert telemarketer(9, 6, 6, 8) == "ignore"


def test_answer():
    assert telemarketer(5, 6, 6, 8) == "answer"
