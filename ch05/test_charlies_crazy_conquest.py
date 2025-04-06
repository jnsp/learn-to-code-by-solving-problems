from charlies_crazy_conquest import make_logs, simulate


def test_make_logs():
    logs_charlie = [("A", 50), ("D", 10), ("A", 100)]
    logs_bot = [("A", 90), ("D", 0), ("A", 0)]

    expected_logs = [("A", 50), ("A", 90), ("D", 10), ("D", 0), ("A", 100), ("A", 0)]
    assert make_logs(logs_charlie, logs_bot) == expected_logs


def test_simulate_1():
    health = 100
    logs_charlie = [("A", 50), ("D", 10), ("A", 100)]
    logs_bot = [("A", 90), ("D", 0), ("A", 0)]

    assert simulate(health, logs_charlie, logs_bot) == "DEFEAT"


def test_simulate_2():
    health = 100
    logs_charlie = [("D", 10), ("D", 20), ("D", 30), ("D", 30)]
    logs_bot = [("D", 10), ("D", 20), ("D", 30), ("D", 40)]

    assert simulate(health, logs_charlie, logs_bot) == "VICTORY"


def test_simulate_3():
    health = 100
    logs_charlie = [("A", 99), ("A", 99)]
    logs_bot = [("D", 1), ("A", 1)]

    assert simulate(health, logs_charlie, logs_bot) == "TIE"
