from happy_or_sad import happy_or_sad


def test_happy():
    test_input = ":-)"
    assert happy_or_sad(test_input) == "happy"


def test_sad():
    test_input = ":-("
    assert happy_or_sad(test_input) == "sad"


def test_none():
    test_input = ":)"
    assert happy_or_sad(test_input) == "none"


def test_unsure():
    test_input = ":-):-("
    assert happy_or_sad(test_input) == "unsure"


def test_happy_anyway():
    test_input = "How are you :-) doing :-( today :-)?"
    assert happy_or_sad(test_input) == "happy"


def test_sad_anyway():
    test_input = "This :-(is str :-(:-a(nge te:-)xt."
    assert happy_or_sad(test_input) == "sad"
