from challenge5 import hex_to_bytes
from challenge5 import bytes_to_hex
from challenge5 import xor
from challenge5 import encrypt


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


def test_encrypt():
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = 'ICE'
    result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f' \
        '20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    assert encrypt(plaintext, key) == result
