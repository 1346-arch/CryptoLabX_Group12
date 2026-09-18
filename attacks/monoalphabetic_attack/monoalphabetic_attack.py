import string

alphabet = string.ascii_uppercase


def frequency_analysis(ciphertext):
    count = {}

    for ch in alphabet:
        count[ch] = 0

    total = 0

    for ch in ciphertext.upper():
        if ch in alphabet:
            count[ch] += 1
            total += 1

    result = []

    for ch in alphabet:
        percentage = (count[ch] / total) * 100 if total else 0
        result.append((ch, count[ch], percentage))

    result.sort(key=lambda x: x[1], reverse=True)

    return result


def word_frequency_analysis(ciphertext):
    words = {}
    word = ""

    for ch in ciphertext.upper() + " ":
        if ch in alphabet:
            word += ch
        else:
            if word:
                words[word] = words.get(word, 0) + 1
                word = ""

    result = list(words.items())
    result.sort(key=lambda x: x[1], reverse=True)

    return result


def word_pattern(word):
    pattern = []
    letters = {}

    number = 0

    for ch in word:
        if ch not in letters:
            letters[ch] = number
            number += 1

        pattern.append(letters[ch])

    return tuple(pattern)


def pattern_analysis(ciphertext):
    words = word_frequency_analysis(ciphertext)
    result = []

    for word, frequency in words:
        result.append(
            (word, frequency, word_pattern(word))
        )

    return result


def apply_substitution(ciphertext, substitutions):
    plaintext = ""

    for ch in ciphertext:
        if ch.upper() in alphabet:

            if ch.upper() in substitutions:
                new_ch = substitutions[ch.upper()]

                if ch.islower():
                    new_ch = new_ch.lower()

                plaintext += new_ch
            else:
                plaintext += "_"

        else:
            plaintext += ch

    return plaintext


def display_partial_plaintext(ciphertext, substitutions):
    plaintext = apply_substitution(ciphertext, substitutions)

    print("\nPartial Plaintext:")
    print(plaintext)

    return plaintext


def verify_solution(ciphertext, plaintext, substitutions):
    reverse = {}

    for cipher, plain in substitutions.items():
        reverse[plain] = cipher

    generated = ""

    for ch in plaintext:
        if ch.upper() in alphabet:
            generated += reverse[ch.upper()]
        else:
            generated += ch

    return generated == ciphertext

def record_decision(step, observation, possible, tested, result, decision):
    print("\nStep:", step)
    print("Observation:", observation)
    print("Possible Substitution:", possible)
    print("Substitution Tested:", tested)
    print("Result:", result)
    print("Decision:", decision)