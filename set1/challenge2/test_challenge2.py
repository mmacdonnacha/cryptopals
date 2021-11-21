from challenge2 import xor


def test_fixedxor():
    given = '1c0111001f010100061a024b53535009181c'
    key = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'

    assert xor(given, key) == expected
