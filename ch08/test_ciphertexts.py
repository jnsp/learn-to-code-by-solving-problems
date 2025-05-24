from ciphertexts import decrypt


def test_decrypt():
    plain_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    cipher_text = "UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH"
    to_decrypt = "XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB"

    expected = "WE ARE VERY BAD PEOPLE DOING VERY BAD THINGS HA HA"
    assert decrypt(plain_text, cipher_text, to_decrypt) == expected


def test_decrypt_not_enough():
    plain_text = "THERE ARE NOT ENOUGH LETTERS"
    cipher_text = "XQAZASEZASNYXSANYLWQSTAXXAZM"
    to_decrypt = "JSCENNYXSIACYIASXQJM"

    expected = ". .ANNOT .E.O.E TH.S"
    assert decrypt(plain_text, cipher_text, to_decrypt) == expected
