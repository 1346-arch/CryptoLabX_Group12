import os
from shift_cipher import decrypt

dictionary_path = os.path.join(
    os.path.dirname(__file__),
    "../../dictionary/english_words.txt"
)

with open(dictionary_path, "r") as file:
    dictionary = set()

    for word in file:
        dictionary.add(word.strip().lower())


def brute_force(ciphertext):
    best_key = 0
    best_text = ""
    best_score = 0

    for key in range(26):
        plaintext = decrypt(ciphertext, key)

        words = plaintext.split()

        score = 0

        for word in words:
            if word.lower() in dictionary:
                score += 1

        print("Key:", key, "Text:", plaintext, "Score:", score)

        if score > best_score:
            best_score = score
            best_key = key
            best_text = plaintext

    return best_key, best_text


ciphertext = "mjqqt btwqi"

key, plaintext = brute_force(ciphertext)

print("\nBest Key:", key)
print("Best Plaintext:", plaintext)