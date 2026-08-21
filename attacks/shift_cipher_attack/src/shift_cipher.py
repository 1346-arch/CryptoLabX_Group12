def encrypt(text, key):

    result = ""

    for char in text:
        result += chr(ord(char) + key) % 26

    return result


def decrypt(text, key):

    return encrypt(text, -key)