from set1.challenge2.challenge2 import Challenge2

import pytest


@pytest.fixture
def chall2():
    return Challenge2()


def test_hex_to_bytes1(chall2):
    given = 'ff'
    expected = b'\xff'

    assert expected == chall2.hex_to_bytes(given)


def test_hex_to_bytes2(chall2):
    given = 'deadbeef'
    expected = b'\xde\xad\xbe\xef'

    assert expected == chall2.hex_to_bytes(given)


def test_bytes_to_hex1(chall2):
    given = b'\xff'
    expected = 'ff'

    assert expected == chall2.bytes_to_hex(given)


def test_bytes_to_hex2(chall2):
    given = b'\xde\xad\xbe\xef'
    expected = 'deadbeef'

    assert expected == chall2.bytes_to_hex(given)


def test_xor(chall2):
    given = 'cafebabe'
    key = 'deadbeef'
    expected = '14530451'

    assert expected == chall2.xor(given, key)


def test_solution(chall2):
    given = '1c0111001f010100061a024b53535009181c'
    key = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'

    assert expected == chall2.xor(given, key)
