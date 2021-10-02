from challenge3 import hex_to_bytes
from challenge3 import bytes_to_hex
from challenge3 import xor
from challenge3 import english_score


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


def test_bytes_to_hex():
    given = b'\x01'
    expected = '01'
    assert bytes_to_hex(given) == expected


def test_bytes_to_hex_given_newline():
    given = b'\n'
    expected = '0a'
    assert bytes_to_hex(given) == expected


def test_bytes_to_hex_given_ff0f():
    given = b'\xff\x0f'
    expected = 'ff0f'
    assert bytes_to_hex(given) == expected


def test_bytes_to_hex_given_deadbeef():
    given = b'\xde\xad\xbe\xef'
    expected = 'deadbeef'
    assert bytes_to_hex(given) == expected


def test_xor_01xor1():
    given = '01'
    expected = '00'
    assert xor(given, 1) == expected


def test_xor_0101xor1():
    given = '0101'
    expected = '0000'
    assert xor(given, 1) == expected


def test_english_score_given_e():
    given = 'e'
    expected = 26
    assert english_score(given) == expected


def test_english_score_given_capital_letter():
    given = 'E'
    expected = 26
    assert english_score(given) == expected


def test_english_score_given_numbers():
    given = '123'
    expected = 0
    assert english_score(given) == expected


def test_english_score_given_hello():
    given = 'hello'
    expected = 100
    assert english_score(given) == expected


def test_english_score_given_phrase():
    given = 'To be or not to be'
    expected = 407
    assert english_score(given) == expected
