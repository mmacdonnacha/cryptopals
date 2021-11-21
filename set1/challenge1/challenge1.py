import binascii
import base64


class challenge1:

    def hex_to_bytes(input: str) -> bytes:
        return binascii.unhexlify(input)
