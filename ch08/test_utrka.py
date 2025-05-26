from utrka import find_not_finished


def test_find_not_finished_distinct_names():
    registered = ["leo", "kiki", "eden"]
    completed = ["eden", "kiki"]
    assert find_not_finished(registered, completed) == "leo"


def test_find_not_finished_duplicated_names():
    registered = [
        "mislav",
        "stanko",
        "mislav",  # duplicated name
        "ana",
    ]
    completed = [
        "stanko",
        "ana",
        "mislav",  # only one completed among duplicates
    ]

    assert find_not_finished(registered, completed) == "mislav"
