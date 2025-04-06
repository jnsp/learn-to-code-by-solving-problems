from crtanje import calculate_net_values, draw_graph, get_levels, prepare_graph


def test_net_values():
    signs = "++---=="
    assert calculate_net_values(signs) == [0, 1, 2, 1, 0, -1, -1, -1]


def test_levels():
    net_values = [0, 1, 2, 1, 0, -1, -1, -1]
    assert get_levels(net_values) == [1, 2, 2, 1, 0, 0, 0]


def test_prepare_graph():
    levels = [1, 2, 2, 1, 0, 0, 0]
    expected = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
    ]
    assert prepare_graph(levels) == expected


def test_draw_graph():
    signs = "++---=="
    expected = [
        [".", "/", "\\", ".", ".", ".", "."],
        ["/", ".", ".", "\\", ".", ".", "."],
        [".", ".", ".", ".", "\\", "_", "_"],
    ]
    assert draw_graph(signs) == expected
