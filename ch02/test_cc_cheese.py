from cc_cheese import cc_cheese


def test_cc_satisfactory():
    assert cc_cheese(2, 70) == "very"
    assert cc_cheese(3, 95) == "absolutely"
    assert cc_cheese(1, 40) == "fairly"
