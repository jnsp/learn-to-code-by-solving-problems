from zigzag import answered_words


def test_answered_words():
    words = ["zagreb", "split", "zadar", "sisak"]
    asked = "zsszz"
    expected = ["zadar", "sisak", "split", "zagreb", "zadar"]
    assert answered_words(words, asked) == expected
