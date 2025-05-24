from marko import count_mappable_words, get_data


def test_count_mappable_words_1():
    words = ["tomo", "mono", "dak"]
    keys_pressed = "6666"
    assert count_mappable_words(words, keys_pressed) == 1


def test_count_mappable_words_2():
    words = ["ja", "la"]
    keys_pressed = "52"
    assert count_mappable_words(words, keys_pressed) == 2


def test_count_mappable_words_3():
    words = ["dom", "fon", "tom"]
    keys_pressed = "366"
    assert count_mappable_words(words, keys_pressed) == 2


def test_get_data(monkeypatch):
    inputs = iter(["3", "tomo", "mono", "dak", "6666"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    words = ["tomo", "mono", "dak"]
    keys_pressed = "6666"
    assert get_data() == (words, keys_pressed)
