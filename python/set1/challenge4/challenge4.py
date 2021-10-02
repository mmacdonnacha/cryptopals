import binascii
import os
import sys


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
            text = ''
            score = 0

        max_score, max_string = check_score(score, text, max_score, max_string)

    return (max_score, max_string)


def read_file(file_name: str) -> list:
    with open(os.path.join(sys.path[0], file_name), "r") as file:
        codes = [f.strip() for f in file.readlines()]

    return codes


def get_best_score_for_each_line(lines: list) -> tuple:
    best_s = 0
    best_t = ''

    for each_line in lines:
        best_fit = [xor(each_line, i) for i in range(0, 255)]
        best_score, best_text = get_highest_score(best_fit)

        best_s, best_t = check_score(best_score, best_text, best_s, best_t)

    return (best_s, best_t)


def check_score(new_score: int, new_text: str, current_score: int, current_text: str) -> tuple:
    if new_score > current_score:
        current_score = new_score
        current_text = new_text

    return (current_score, current_text)


if __name__ == '__main__':
    codes = read_file('input')
    score, text = get_best_score_for_each_line(codes)

    print(f'{score} : {text}')
