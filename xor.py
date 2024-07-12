#!/usr/bin/env python3

import os

def convertAscii(input_str):
    deci_input = ord(input_str)
    bin_input = bin(deci_input).replace("0b", "")
    clean_input = map(str, bin_input)
    clean_input = list(clean_input)
    return clean_input

def main():
    # Get user input
    text = input("Gimme some input: ")
    key = input("Gimme a key: ")

    # Make empty lists
    plaintext = []
    secret_key = []
    ciphertext = []

    if not text.isascii() and not key.isascii():
        # Put user input in list
        for i in text:
            plaintext.append(int(i))

        for i in key:
            secret_key.append(int(i))
    else:
        text = convertAscii(text)
        key = convertAscii(key)

        for i in text:
            plaintext.append(int(i))

        for i in key:
            secret_key.append(int(i))

    # Make list length equal for operation
    if len(plaintext) < len(secret_key):
        result = len(secret_key) - len(plaintext)
        for i in range(result):
            plaintext.insert(0, 0)

    else:
        result = len(plaintext) - len(secret_key)
        for i in range(result):
            secret_key.insert(0, 0)

    # Get ciphertext from XOR operation
    for x,y in zip(plaintext, secret_key):
        if x == y:
            ciphertext.append(0)
        else:
            ciphertext.append(1)

    # Make ciphertext pretty
    pretty_ci = ''.join(map(str, ciphertext))

    # Convert bits to decimal
    deci_ciphertext = int(''.join(map(str, ciphertext)), 2)
    int

    # Clear screen pre-print
    os.system('clear')

    print(f"The ciphertext is: {pretty_ci}")
    print(f"Decimal value: {deci_ciphertext}")

if __name__ == '__main__':
    main()
