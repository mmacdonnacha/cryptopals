from challenge1 import hex_to_bytes
from challenge1 import hex_to_base64


def test_hex_to_bytes():
    given = '01'
    expected = b'\x01'
    assert hex_to_bytes(given) == expected


def test_hex_to_bytes_given_0x0a():
    given = '0a'
    expected = b'\n'
    assert hex_to_bytes(given) == expected


def test_hex_to_bytes_given_0xff0f():
    given = 'ff0f'
    expected = b'\xff\x0f'
    assert hex_to_bytes(given) == expected


def test_hex_to_bytes_given_0xdeadbeef():
    given = 'deadbeef'
    expected = b'\xde\xad\xbe\xef'
    assert hex_to_bytes(given) == expected


def test_hex_to_base64():
    given = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    assert hex_to_base64(given) == expected
