import binascii


class Challenge3():

    def hex_to_bytes(self, input: str) -> bytes:
        '''Convert hexadecimal string into bytes'''
        return binascii.unhexlify(input)

    def bytes_to_hex(self, input: bytes) -> str:
        '''Convert bytes to hexadecimal string'''
        return binascii.hexlify(input).decode('UTF-8')

    def xor(self, hex_string: str, key: int) -> str:
        '''XOR each byte of hex_string with key'''
        output = [(x ^ key) for x in self.hex_to_bytes(hex_string)]

        return self.bytes_to_hex(bytes(output))

    def english_score(self, text: str) -> int:
        '''Calculate how close to english a piece of text is'''
        common_letters = ' etaoinshrdlucmfwypvbgkjqxz'
        score = 0

        for c in text.lower():
            if c in common_letters:
                score = score + (len(common_letters) - common_letters.index(c))
        return score

    def get_highest_score(self, values: list) -> tuple:
        '''Loop through a list of XORed text and
        find the one with highest english score

        return XORed text with highest score'''
        max_score = 0
        max_string = ''

        for h in values:
            try:
                text = bytearray.fromhex(h).decode('utf-8')
                score = self.english_score(text)
            except UnicodeDecodeError:
                score = 0

            if score > max_score:
                max_score = score
                max_string = text

        return (max_score, max_string)

    def solve(self, hex_string):
        '''Solve Challenge 3
        return tuple with (score, text)'''
        list_of_xored_hex_values = [self.xor(hex_string, i) for i in range(0, 255)]
        max_score, max_string = self.get_highest_score(list_of_xored_hex_values)

        return(max_score, max_string)
