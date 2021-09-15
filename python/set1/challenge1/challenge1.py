import binascii
import base64


def hex_to_bytes(input: str) -> bytes:
    return binascii.unhexlify(input)


def hex_to_base64(input: str) -> str:
    h_to_b = hex_to_bytes(input)
    base64_string = base64.b64encode(h_to_b).decode()
    return base64_string


if __name__ == '__main__':
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    converted = hex_to_base64(hex_string)
    print(f'Given     : {hex_string}')
    print(f'Converted : {converted}')
    print(f'Answer    : {base64_string}')
    print(f'Converted == Answer : {converted == base64_string}')
