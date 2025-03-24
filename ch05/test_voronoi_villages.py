from voronoi_villages import smallest_size


def test_smallest_size():
    locations = [16, 0, 10, 4, 15]
    assert smallest_size(locations) == 3.0
