import string

alphabet = string.ascii_uppercase

KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"


def encrypt(plaintext, key):
    ciphertext = ""

    for ch in plaintext:
        if ch.upper() in alphabet:
            pos = alphabet.index(ch.upper())
            new_ch = key[pos]

            if ch.islower():
                new_ch = new_ch.lower()

            ciphertext += new_ch
        else:
            ciphertext += ch

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""

    for ch in ciphertext:
        if ch.upper() in alphabet:
            pos = key.index(ch.upper())
            new_ch = alphabet[pos]

            if ch.islower():
                new_ch = new_ch.lower()

            plaintext += new_ch
        else:
            plaintext += ch

    return plaintext