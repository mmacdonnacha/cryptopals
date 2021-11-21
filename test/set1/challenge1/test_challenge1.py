from set1.challenge1.challenge1 import Challenge1

import pytest


@pytest.fixture(autouse=True)
def chall1():
    return Challenge1()


def test_hex_to_bytes1(chall1):
    given = 'FF'
    expected = b'\xFF'

    assert expected == chall1.hex_to_bytes(given)


def test_hex_to_bytes2(chall1):
    given = 'DEADBEEF'
    expected = b'\xde\xad\xbe\xef'

    assert expected == chall1.hex_to_bytes(given)


def test_hex_to_base64_1(chall1):
    given = 'FF'
    expected = '/w=='

    assert expected == chall1.hex_to_base64(given)


def test_hex_to_base64_2(chall1):
    given = 'DEADBEEF'
    expected = '3q2+7w=='

    assert expected == chall1.hex_to_base64(given)


def test_solution(chall1):
    given = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    assert expected == chall1.hex_to_base64(given)
