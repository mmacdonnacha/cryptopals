import pytest
import set1.challenge1.challenge1


@pytest.fixture
def setup():
    chall1 = challenge1()
    return chall1


def test_hex_to_bytes(setup):
    given = chall1.hex_to_bytes('01')
    expected = b'\x01'

    assert given == expected


# def test_hex_to_bytes_given_0x0a():
#     given = '0a'
#     expected = b'\n'
#     assert hex_to_bytes(given) == expected


# def test_hex_to_bytes_given_0xff0f():
#     given = 'ff0f'
#     expected = b'\xff\x0f'
#     assert hex_to_bytes(given) == expected


# def test_hex_to_bytes_given_0xdeadbeef():
#     given = 'deadbeef'
#     expected = b'\xde\xad\xbe\xef'
#     assert hex_to_bytes(given) == expected