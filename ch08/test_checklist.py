from checklist import complete_assignments, get_items_and_assignments


def test_complete_assignments():
    items = {"chalk", "cheese", "charger"}
    assignments = [
        ["cheese"],
        ["coins", "cash"],
        ["charger", "chalk", "caffeine"],
        ["cheese", "charger", "cheese"],
    ]
    assert complete_assignments(items, assignments) == 2


def test_get_items_and_assignments(monkeypatch):
    inputs = iter(
        [
            "3 4",
            "chalk",
            "cheese",
            "charger",
            "1",
            "cheese",
            "2",
            "coins",
            "cash",
            "3",
            "charger",
            "chalk",
            "caffeine",
            "3",
            "cheese",
            "charger",
            "cheese",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    items = {"chalk", "cheese", "charger"}
    assignments = [
        ["cheese"],
        ["coins", "cash"],
        ["charger", "chalk", "caffeine"],
        ["cheese", "charger", "cheese"],
    ]

    assert get_items_and_assignments() == (items, assignments)
