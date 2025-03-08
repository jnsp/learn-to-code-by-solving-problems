from cone_volume import cone_volume


def test_cone_volume():
    assert cone_volume(4, 6) == 100.53096491487338
    assert cone_volume(4, 5) == 83.7758040957278
    assert cone_volume(1, 1) == 1.0471975511965976
    assert cone_volume(0, 0) == 0.0
    assert cone_volume(1, 0) == 0.0
    assert cone_volume(0, 1) == 0.0
