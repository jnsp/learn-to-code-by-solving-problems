from kemija import decode


def test_decode_1():
    encoded = "zepelepenapa papapripikapa"
    decoded = "zelena paprika"
    assert decode(encoded) == decoded


def test_decode_2():
    encoded = "bapas jepe doposapadnapa opovapa kepemipijapa"
    decoded = "bas je dosadna ova kemija"
    assert decode(encoded) == decoded
