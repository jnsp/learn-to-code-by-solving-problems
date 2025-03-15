from magnus import honi


def test_magnus():
    assert honi("MAGNUS") == 0


def test_honi():
    assert honi("HHHHOOOONNNNIIII") == 1


def test_double_honi():
    assert honi("PROHODNIHODNIK") == 2
