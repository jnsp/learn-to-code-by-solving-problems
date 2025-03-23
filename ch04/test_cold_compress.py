from cold_compress import encode


def test_encode_simple():
    target_string = "+++===!!!!"
    expected_encoded = [("+", 3), ("=", 3), ("!", 4)]

    assert encode(target_string) == expected_encoded


def test_encode_non_trivial():
    target_string = "(AABBC)"
    expected_encoded = [("(", 1), ("A", 2), ("B", 2), ("C", 1), (")", 1)]

    assert encode(target_string) == expected_encoded


def test_encode_complicated():
    target_string = "3.1415555"
    expected_encoded = [("3", 1), (".", 1), ("1", 1), ("4", 1), ("1", 1), ("5", 4)]

    assert encode(target_string) == expected_encoded
