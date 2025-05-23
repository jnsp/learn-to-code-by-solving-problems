from collections import Counter

from common_words import common_words, get_kth_most_common_words, invert_counter, kth_notation


def test_invert_counter():
    words = ["the", "brown", "the", "fox", "red", "the", "red"]
    counter = Counter(words)
    assert invert_counter(counter) == {3: ["the"], 2: ["red"], 1: ["brown", "fox"]}


def test_get_kth_most_common_words():
    inverted_counter = {3: ["the"], 2: ["red"], 1: ["brown", "fox"]}
    assert get_kth_most_common_words(inverted_counter, 1) == ["the"]
    assert get_kth_most_common_words(inverted_counter, 2) == ["red"]
    assert get_kth_most_common_words(inverted_counter, 3) == ["brown", "fox"]
    assert get_kth_most_common_words(inverted_counter, 4) is None


def test_common_words():
    words = ["the", "brown", "the", "fox", "red", "the", "red"]
    assert common_words(words, 2) == ["red"]


def test_kth_notation():
    assert kth_notation(1) == "1st"
    assert kth_notation(2) == "2nd"
    assert kth_notation(3) == "3rd"
    assert kth_notation(4) == "4th"
    assert kth_notation(11) == "11th"
    assert kth_notation(12) == "12th"
    assert kth_notation(13) == "13th"
    assert kth_notation(21) == "21st"
    assert kth_notation(22) == "22nd"
    assert kth_notation(23) == "23rd"
    assert kth_notation(1013) == "1013th"
