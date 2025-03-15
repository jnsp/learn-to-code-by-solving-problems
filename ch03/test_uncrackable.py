from uncrackable import valid_password


def test_valid_password():
    assert valid_password("PassW0rd") == "Valid"


def test_invalid_password():
    assert valid_password("CorrectHorseBatteryStaple") == "Invalid"
