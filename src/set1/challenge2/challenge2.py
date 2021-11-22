import binascii


class Challenge2():

    def hex_to_bytes(self, input: str) -> bytes:
        '''Convert hexadecimal string into bytes'''
        return binascii.unhexlify(input)

    def bytes_to_hex(self, input: bytes) -> str:
        '''Convert bytes to hexadecimal string'''
        return binascii.hexlify(input).decode('UTF-8')

    def xor(self, hex_string: str, key: str) -> str:
        '''Perform byte level XOR on hex_string using key'''
        output = []
        bytes_hex_string = self.hex_to_bytes(hex_string)
        bytes_key = self.hex_to_bytes(key)
        for x, y in zip(bytes_hex_string, bytes_key):
            output.append(x ^ y)

        return self.bytes_to_hex(bytes(output))
