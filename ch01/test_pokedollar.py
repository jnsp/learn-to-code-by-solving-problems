from pokedollar import pokedollar


def test_pokedollar():
    p = 14
    b = 3
    d = 10
    assert pokedollar(p, b, d) == 42
