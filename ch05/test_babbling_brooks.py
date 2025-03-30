from babbling_brooks import join, split


def test_split_fisrt_stream():
    test_streams = [10, 20, 30]
    to_split = 1
    percentage = 50

    assert split(test_streams, to_split, percentage) == [5, 5, 20, 30]


def test_split_last_stream():
    test_streams = [10, 20, 30]
    to_split = 3
    percentage = 50

    assert split(test_streams, to_split, percentage) == [10, 20, 15, 15]


def test_split_mid_stream():
    test_streams = [10, 20, 30]
    to_split = 2
    percentage = 50

    assert split(test_streams, to_split, percentage) == [10, 10, 10, 30]


def test_join_first_stream():
    test_streams = [5, 5, 20, 30]
    to_join = 1

    assert join(test_streams, to_join) == [10, 20, 30]


def test_join_mid_stream():
    test_streams = [5, 5, 20, 30]
    to_join = 2

    assert join(test_streams, to_join) == [5, 25, 30]


def test_join_last_stream():
    test_streams = [5, 5, 20, 30]
    to_join = 3

    assert join(test_streams, to_join) == [5, 5, 50]
