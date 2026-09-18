import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classical.monoalphabetic_cipher import encrypt, KEY


input_file = "datasets/monoalphabetic_plaintext.txt"
output_file = "outputs/monoalphabetic/ciphertext.txt"


with open(input_file, "r", encoding="utf-8") as file:
    plaintext = file.read()


ciphertext = encrypt(plaintext, KEY)


with open(output_file, "w", encoding="utf-8") as file:
    file.write(ciphertext)


print("Encryption completed.")
print("Plaintext :", input_file)
print("Ciphertext:", output_file)