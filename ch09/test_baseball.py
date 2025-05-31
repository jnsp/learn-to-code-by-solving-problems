from baseball import count_triples


def test_count_triples1():
    positions = [3, 1, 10, 7, 4]
    assert count_triples(positions) == 4


def test_count_triples2():
    positions = [16, 14, 23, 18, 1, 6, 11]
    assert count_triples(positions) == 11
