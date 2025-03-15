from english_or_french import detect_lang


def test_english():
    text = "The red cat sat on the mat. Why are you so sad cat? Don't ask that."
    assert detect_lang(text) == "English"


def test_french():
    text = "Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre"
    assert detect_lang(text) == "French"


def test_english_but_french():
    text = "Si je discernais ta voix encore Connaissant ce coeur qui doute, Tu me dirais de tirer un trait Quoi que partir me coute."
    assert detect_lang(text) == "English"
