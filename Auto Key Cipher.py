UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"

def is_upper(char):
    for i in range(26):
        if UPPER[i] == char:
            return True
    return False

def is_lower(char):
    for i in range(26):
        if LOWER[i] == char:
            return True
    return False

def is_letter(char):
    return is_upper(char) or is_lower(char)

def to_upper(char):
    for i in range(26):
        if LOWER[i] == char:
            return UPPER[i]
    return char

def get_index(char):
    for i in range(26):
        if UPPER[i] == char or LOWER[i] == char:
            return i
    return -1

def mod26(n):
    while n < 0:
        n = n + 26
    while n >= 26:
        n = n - 26
    return n

def get_letter(index, use_upper):
    if use_upper:
        return UPPER[index]
    else:
        return LOWER[index]


# -------------------------
# Encryption
# -------------------------
def vigenere_autokey_encrypt(plaintext, keyword):

    result = ""
    key_index = 0

    key_stream = []
    for i in range(len(keyword)):
        key_stream = key_stream + [to_upper(keyword[i])]

    plain_letters = []
    for i in range(len(plaintext)):
        if is_letter(plaintext[i]):
            plain_letters = plain_letters + [to_upper(plaintext[i])]

    full_key = key_stream + plain_letters

    for i in range(len(plaintext)):
        char = plaintext[i]

        if is_letter(char):

            char_index = get_index(char)

            key_char = full_key[key_index]
            key_shift = get_index(key_char)

            new_index = mod26(char_index + key_shift)

            result = result + get_letter(new_index, is_upper(char))

            key_index = key_index + 1
        else:
            result = result + char

    return result


# -------------------------
# Decryption
# -------------------------
def vigenere_autokey_decrypt(ciphertext, keyword):

    result = ""
    key_index = 0

    key_stream = []
    for i in range(len(keyword)):
        key_stream = key_stream + [to_upper(keyword[i])]

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if is_letter(char):

            char_index = get_index(char)

            key_char = key_stream[key_index]
            key_shift = get_index(key_char)

            new_index = mod26(char_index - key_shift)

            plain_char = get_letter(new_index, is_upper(char))

            result = result + plain_char

            # Add decrypted letter to key
            key_stream = key_stream + [to_upper(plain_char)]

            key_index = key_index + 1

        else:
            result = result + char

    return result