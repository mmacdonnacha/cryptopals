import binascii


def hex_to_bytes(input: str) -> bytes:
    return binascii.unhexlify(input)


def bytes_to_hex(input: bytes) -> str:
    return binascii.hexlify(input).decode()


def xor(hex_string: str, key: int) -> str:
    output = [x ^ key for x in hex_to_bytes(hex_string)]

    return bytes_to_hex(bytes(output))


def encrypt(plaintext: str, key: str) -> str:
    p_bytes = bytes(plaintext, 'utf-8')
    k_bytes = bytes(key, 'utf-8')

    encrypted = []
    index = 0

    for x in p_bytes:
        encrypted.append(x ^ k_bytes[index])
        index = (index + 1) % 3

    return bytes_to_hex(bytes(encrypted))


if __name__ == '__main__':
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = 'ICE'
    result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f' \
        '20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    my_answer = encrypt(plaintext, key)
    print(result)
    print(my_answer)
    print(result == my_answer)
