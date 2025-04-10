import pytest
from action_figures import box_ok, check_endpoints, endpoints, read_box


def test_read_box(monkeypatch):
    inputs = iter(["3", "2 1 2", "3 7 7 7", "1 5"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    actual = read_box()
    expected = [[1, 2], [7, 7, 7], [5]]

    assert expected == actual


@pytest.mark.parametrize(
    "box, expected",
    [
        ([1, 2, 3], True),
        ([4], True),
        ([2, 2, 2], True),
        ([4, 1], False),
    ],
)
def test_box_ok(box, expected):
    assert box_ok(box) == expected


def test_endpoints():
    boxes = [[1, 2], [7, 7, 7], [5]]
    expected = [[1, 2], [7, 7], [5, 5]]
    assert endpoints(boxes) == expected


def test_check_endpoints():
    right_endpoints = [[1, 6], [9, 25], [32, 36]]
    assert check_endpoints(right_endpoints)

    wrong_endpoints = [[1, 6], [9, 50], [32, 36]]
    assert not check_endpoints(wrong_endpoints)
