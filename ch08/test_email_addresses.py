from email_addresses import count_unique_emails, get_emails, remove_after_plus, remove_dot


def test_remove_dot():
    email = "foo.bar@baz.com"
    assert remove_dot(email) == "foobar@baz.com"


def test_remove_plus():
    email = "fO.o+baz123@bAR.com"
    assert remove_after_plus(email) == "fO.o@bAR.com"


def test_count_unique_emails():
    emails = [
        "foo@bar.com",
        "fO.o+baz123@bAR.com",
        "foo@bar..com",
    ]

    assert count_unique_emails(emails) == 2


def test_get_emails(monkeypatch):
    inputs = iter(["3", "email1", "email2", "email3"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    actual = get_emails()
    expected = ["email1", "email2", "email3"]

    assert expected == actual
