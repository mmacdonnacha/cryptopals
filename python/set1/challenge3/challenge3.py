import binascii


def hex_to_bytes(input: str) -> bytes:
    return binascii.unhexlify(input)


def bytes_to_hex(input: bytes) -> str:
    return binascii.hexlify(input).decode()


def xor(hex_string: str, key: int) -> str:
    output = [(x ^ key) for x in hex_to_bytes(hex_string)]

    return bytes_to_hex(bytes(output))


def english_score(text: str) -> int:
    common_letters = ' etaoinshrdlucmfwypvbgkjqxz'
    score = 0

    for c in text.lower():
        if c in common_letters:
            score = score + (len(common_letters) - common_letters.index(c))
    return score


def get_highest_score(values: list) -> tuple:
    max_score = 0
    max_string = ''

    for h in values:
        try:
            text = bytearray.fromhex(h).decode('utf-8')
            score = english_score(text)
        except UnicodeDecodeError:
            score = 0

        if score > max_score:
            max_score = score
            max_string = text

    return (max_score, max_string)


if __name__ == '__main__':
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    list_of_xored_hex_values = [xor(hex_string, i) for i in range(0, 255)]

    max_score, max_string = get_highest_score(list_of_xored_hex_values)

    print(f'{max_score} : {max_string}')
