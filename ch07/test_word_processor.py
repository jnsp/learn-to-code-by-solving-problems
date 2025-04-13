from word_processor import edit


def test_word_processor():
    width = 7
    words = "hello my name is Bessie and this is my essay"

    expected = [
        "hello my",
        "name is",
        "Bessie",
        "and this",
        "is my",
        "essay",
    ]

    assert edit(words, width) == expected
