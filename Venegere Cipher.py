UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_index(char):
    for i in range(26):
        if UPPER[i] == char:
            return i
    return -1


def vigenere_encrypt(plaintext, key):

    plaintext = plaintext.upper()
    key = key.upper()

    result = ""
    key_index = 0

    for i in range(len(plaintext)):

        char = plaintext[i]

        if char in UPPER:

            p = get_index(char)
            k = get_index(key[key_index % len(key)])

            c = (p + k) % 26

            result = result + UPPER[c]

            key_index = key_index + 1

        else:
            result = result + char

    return result


def vigenere_decrypt(ciphertext, key):

    ciphertext = ciphertext.upper()
    key = key.upper()

    result = ""
    key_index = 0

    for i in range(len(ciphertext)):

        char = ciphertext[i]

        if char in UPPER:

            c = get_index(char)
            k = get_index(key[key_index % len(key)])

            p = (c - k) % 26

            result = result + UPPER[p]

            key_index = key_index + 1

        else:
            result = result + char

    return result


message = "CRYPTOGRAPHY"
key = "KEY"

encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Plaintext :", message)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)