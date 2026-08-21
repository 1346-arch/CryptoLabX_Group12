from shift_cipher import decrypt


# English letter frequencies
english_frequency = {
    'a': 8.17,
    'b': 1.49,
    'c': 2.78,
    'd': 4.25,
    'e': 12.70,
    'f': 2.23,
    'g': 2.02,
    'h': 6.09,
    'i': 6.97,
    'j': 0.15,
    'k': 0.77,
    'l': 4.03,
    'm': 2.41,
    'n': 6.75,
    'o': 7.51,
    'p': 1.93,
    'q': 0.10,
    'r': 5.99,
    's': 6.33,
    't': 9.06,
    'u': 2.76,
    'v': 0.98,
    'w': 2.36,
    'x': 0.15,
    'y': 1.97,
    'z': 0.07
}


def chi_square(text):

    count = {}

    for letter in english_frequency:
        count[letter] = 0

    for char in text:
        if char in count:
            count[char] += 1

    total = sum(count.values())

    if total == 0:
        return float("inf")

    score = 0

    for letter in english_frequency:

        expected = (
            english_frequency[letter] / 100
        ) * total

        observed = count[letter]

        score += (
            (observed - expected) ** 2
        ) / expected

    return score


def chi_square_attack(ciphertext):

    best_key = 0
    best_text = ""
    best_score = float("inf")

    for key in range(26):

        plaintext = decrypt(ciphertext, key)

        score = chi_square(plaintext)

        print(
            "Key:", key,
            "Text:", plaintext,
            "Score:", round(score, 2)
        )

        if score < best_score:

            best_score = score
            best_key = key
            best_text = plaintext

    return best_key, best_text


# Test
ciphertext = "ymj vznjy qfpj rnwwtwji ymj jajsnsl xyfwx"

key, plaintext = chi_square_attack(ciphertext)

print("\nBest Key:", key)
print("Best Plaintext:", plaintext)
