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

def caesar_encrypt(plaintext, shift):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if is_letter(char):
            index = get_index(char)
            new_index = mod26(index + shift)
            result = result + get_letter(new_index, is_upper(char))
        else:
            result = result + char

    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


message = "Hello World"
shift = 3

encrypted = caesar_encrypt(message, shift)
decrypted =print("Decrypted:", decrypted)