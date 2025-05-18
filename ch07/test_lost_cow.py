import pytest
from lost_cow import travel


@pytest.mark.parametrize(
    "farmer, cow, output",
    [
        (3, 6, 9),
        (7, 5, 4),
        (93, 35, 312),
        (86, 92, 36),
        (690, 59, 4725),
        (540, 426, 368),
        (172, 736, 2610),
    ],
)
def test_travel_distance(farmer, cow, output):
    assert travel(farmer, cow) == output
