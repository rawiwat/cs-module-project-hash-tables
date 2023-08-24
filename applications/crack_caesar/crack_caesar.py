# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import math
from collections import Counter
# Your code here
from string import ascii_lowercase

ALPHABET = ascii_lowercase
ALPHABET_SIZE = 26
Frequency = {'e': 11.53, 't': 9.75, 'a': 8.46, 'o': 8.08, 'h': 7.71, 'n': 6.73,
             'r': 6.29, 'i': 5.84, 's': 5.56, 'd': 4.74, 'l': 3.92, 'w': 3.08,
             'u': 2.59, 'g': 2.48, 'f': 2.42, 'b': 2.19, 'm': 2.18, 'y': 2.02,
             'c': 1.58, 'p': 1.08, 'k': 0.84, 'v': 0.59, 'q': 0.17, 'j': 0.07,
             'x': 0.07, 'z': 0.03
             }


def decrypt(text: str, key: int) -> str:
    result = ''

    for char in text:
        if not char.isalpha():
            result += char
            continue

        index = ALPHABET.index(char.lower())
        new_char = ALPHABET[(index - key) % ALPHABET_SIZE]
        result += new_char.upper() if char.isupper() else new_char

    return result


def encrypt(text: str, key: int) -> str:
    result = ''

    for char in text:
        if not char.isalpha():
            result += char
            continue

        index = ALPHABET.index(char.lower())
        new_char = ALPHABET[(index + key) % ALPHABET_SIZE]
        result += new_char.upper() if char.isupper() else new_char

    return result


def difference(text: str) -> float:
    counter = Counter(text)
    return sum(
        [abs(counter.get(letter, 0) * 100 / len(text) - Frequency[letter]) for letter in ALPHABET]) / ALPHABET_SIZE


def cipher(text: str) -> int:
    lowest_diff = math.inf
    encrypt_key = 0

    for key in range(1, ALPHABET_SIZE):
        current_plain_text = decrypt(text, key)
        current_diff = difference(current_plain_text)

        if current_diff < lowest_diff:
            lowest_diff = current_diff
            encrypt_key = key

    return encrypt_key


with open('ciphertext.txt', 'r') as file:
    file_content = file.read()

ciphered_text = cipher(file_content)
encrypted_text = encrypt(file_content, ciphered_text)

print(encrypted_text)
