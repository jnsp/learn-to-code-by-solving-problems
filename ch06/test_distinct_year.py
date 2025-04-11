from distinct_year import is_distinct, next_distinct_year, read_year


def test_is_distinct():
    distinct_year = 1987
    assert is_distinct(distinct_year)

    not_distinct_year = 999
    assert not is_distinct(not_distinct_year)


def test_next_distinct_year():
    year = 1987
    assert next_distinct_year(year) == 2013

    year = 999
    assert next_distinct_year(year) == 1023


def test_read_year(monkeypatch):
    input_value = "1987"
    monkeypatch.setattr("builtins.input", lambda *arg: input_value)
    assert read_year() == 1987
