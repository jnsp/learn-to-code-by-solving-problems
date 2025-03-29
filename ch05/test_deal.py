from deal import expected_value


def test_deal():
    assert expected_value([3, 8]) == 198825
