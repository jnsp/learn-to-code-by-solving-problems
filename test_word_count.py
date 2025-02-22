from word_count import word_count


def test_one_word_string():
    test_string = "Hello"
    assert word_count(test_string) == 1


def test_two_words_string():
    test_string = "Hello World"
    assert word_count(test_string) == 2


def test_long_string():
    test_string = "Hello World, how are you today?"
    assert word_count(test_string) == 6


def test_empty_string():
    test_string = ""
    assert word_count(test_string) == 0
