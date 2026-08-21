def encrypt(text, key):

    result = ""

    for char in text:
        if char == " ":
            result += " "

        else:
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

    return result


def decrypt(text, key):

    return encrypt(text, -key)

print(encrypt("the quiet lake mirrored the evening stars", 5))
print(decrypt(encrypt("hello world in python", 5), 5))