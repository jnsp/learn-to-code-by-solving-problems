from three_cups import three_cups


def test_three_cups():
    assert three_cups("AB") == 3
    assert three_cups("CBABCACCC") == 1
