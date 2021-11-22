from set1.challenge3.challenge3 import Challenge3

import pytest


@pytest.fixture
def chall3():
    return Challenge3()


def test_hex_to_bytes1(chall3):
    given = 'ff'
    expected = b'\xff'

    assert expected == chall3.hex_to_bytes(given)


def test_hex_to_bytes2(chall3):
    given = 'deadbeef'
    expected = b'\xde\xad\xbe\xef'

    assert expected == chall3.hex_to_bytes(given)


def test_bytes_to_hex1(chall3):
    given = b'\xff'
    expected = 'ff'

    assert expected == chall3.bytes_to_hex(given)


def test_bytes_to_hex2(chall3):
    given = b'\xde\xad\xbe\xef'
    expected = 'deadbeef'

    assert expected == chall3.bytes_to_hex(given)


def test_xor_01xor1(chall3):
    given = '01'
    key = 1
    expected = '00'

    assert expected == chall3.xor(given, key)


def test_xor_0101xor1(chall3):
    given = '0101'
    key = 1
    expected = '0000'

    assert expected == chall3.xor(given, key)


def test_english_score_given_e(chall3):
    given = 'e'
    expected = 26

    assert expected == chall3.english_score(given)


def test_english_score_given_capital_letter(chall3):
    given = 'E'
    expected = 26

    assert expected == chall3.english_score(given)


def test_english_score_given_numbers(chall3):
    given = '123'
    expected = 0

    assert expected == chall3.english_score(given)


def test_english_score_given_hello(chall3):
    given = 'hello'
    expected = 100

    assert expected == chall3.english_score(given)


def test_english_score_given_phrase(chall3):
    given = 'To be or not to be'
    expected = 407

    assert expected == chall3.english_score(given)


def test_solution(chall3):
    given = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    expected = (625, "Cooking MC's like a pound of bacon")

    assert expected == chall3.solve(given)
