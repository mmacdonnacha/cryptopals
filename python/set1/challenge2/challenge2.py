import binascii


def hex_to_bytes(input: str) -> bytes:
    return binascii.unhexlify(input)


def bytes_to_hex(input: bytes) -> str:
    return binascii.hexlify(input).decode()


def xor(hex_string: str, key: str) -> str:
    output = []
    bytes_hex_string = hex_to_bytes(hex_string)
    bytes_key = hex_to_bytes(key)
    for x, y in zip(bytes_hex_string, bytes_key):
        output.append(x ^ y)

    return bytes_to_hex(bytes(output))


if __name__ == '__main__':
    hex_string = '1c0111001f010100061a024b53535009181c'
    key = '686974207468652062756c6c277320657965'
    expected_answer = '746865206b696420646f6e277420706c6179'

    print(f'Expected : {expected_answer}')
    print(f'Answer  : {xor(hex_string, key)}')
    print(f'Expected == Answer : {expected_answer == xor(hex_string, key)}')
