from ljestvica import decide_scale


def test_decide_scale():
    assert decide_scale("AEB|C") == "C-dur"
    assert decide_scale("CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C") == "C-dur"
