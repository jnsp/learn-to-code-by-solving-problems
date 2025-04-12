from platforme import Platform, length_of_pillars, total_length


def test_Platform():
    p = Platform(1, 5, 10)

    assert p.left_pillar == 5.5
    assert p.right_pillar == 9.5

    higher_p = Platform(3, 1, 5)
    assert p < higher_p

    assert higher_p - p == 2


def test_get_pillars_1():
    platforms = [Platform(1, 5, 10), Platform(3, 1, 5), Platform(5, 3, 7)]
    target_platform = Platform(1, 5, 10)
    assert length_of_pillars(target_platform, platforms) == 2


def test_get_pillars_2():
    platforms = [Platform(1, 5, 10), Platform(3, 1, 5), Platform(5, 3, 7)]
    target_platform = Platform(3, 1, 5)
    assert length_of_pillars(target_platform, platforms) == 6


def test_get_pillars_3():
    platforms = [Platform(1, 5, 10), Platform(3, 1, 5), Platform(5, 3, 7)]
    target_platform = Platform(5, 3, 7)
    assert length_of_pillars(target_platform, platforms) == 6


def test_get_pillars_4():
    platforms = [
        Platform(50, 50, 90),
        Platform(40, 40, 80),
        Platform(30, 30, 70),
        Platform(20, 20, 60),
        Platform(10, 10, 50),
    ]
    target_platform = Platform(50, 50, 90)
    assert length_of_pillars(target_platform, platforms) == 60


def test_total_length_1():
    platforms = [Platform(1, 5, 10), Platform(3, 1, 5), Platform(5, 3, 7)]
    assert total_length(platforms) == 14


def test_total_length_2():
    platforms = [
        Platform(50, 50, 90),
        Platform(40, 40, 80),
        Platform(30, 30, 70),
        Platform(20, 20, 60),
        Platform(10, 10, 50),
    ]
    assert total_length(platforms) == 200
