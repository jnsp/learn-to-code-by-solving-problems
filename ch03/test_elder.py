from elder import obey_who


def test_obey_who1():
    original_wizard = "A"
    duels = [("B", "A"), ("C", "B"), ("D", "A")]
    assert obey_who(original_wizard, duels) == ("C", 3)


def test_obey_who2():
    original_wizard = "N"
    duels = [("D", "A"), ("N", "B"), ("B", "A"), ("C", "D"), ("F", "A")]
    assert obey_who(original_wizard, duels) == ("N", 1)
