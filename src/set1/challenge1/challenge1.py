import binascii
import base64


class Challenge1():

    def hex_to_bytes(self, input: str) -> bytes:
        '''Convert hexadecimal string into bytes'''
        return binascii.unhexlify(input)

    def hex_to_base64(self, input: str) -> str:
        '''Convert hexadecimal string to base64 string'''
        hex_bytes = self.hex_to_bytes(input)
        base64_string = base64.b64encode(hex_bytes).decode()
        return base64_string
