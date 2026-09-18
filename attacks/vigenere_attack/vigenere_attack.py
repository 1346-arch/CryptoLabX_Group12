import string


def clean_ciphertext(ciphertext):
    cleaned = ""

    for ch in ciphertext.upper():
        if ch in string.ascii_uppercase:
            cleaned += ch

    return cleaned

def find_repeated_patterns(ciphertext):
    patterns = {}

    for length in range(3, 6):
        for i in range(len(ciphertext) - length + 1):
            pattern = ciphertext[i:i + length]

            if pattern not in patterns:
                patterns[pattern] = []

            patterns[pattern].append(i)

    repeated = {}

    for pattern in patterns:
        if len(patterns[pattern]) > 1:
            repeated[pattern] = patterns[pattern]

    return repeated


def calculate_distances(repeated_patterns):
    distances = []

    for pattern in repeated_patterns:
        positions = repeated_patterns[pattern]

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                distance = positions[j] - positions[i]

                distances.append((pattern, distance))

    return distances


def find_factors(number):
    factors = []

    for i in range(2, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

def kasiski_analysis(ciphertext):
    repeated_patterns = find_repeated_patterns(ciphertext)
    distances = calculate_distances(repeated_patterns)

    factor_count = {}

    for pattern, distance in distances:
        factors = find_factors(distance)

        for factor in factors:
            if factor <= 20:
                factor_count[factor] = factor_count.get(factor, 0) + 1

    result = list(factor_count.items())
    result.sort(key=lambda x: x[1], reverse=True)

    return result

def calculate_ic(text):
    n = len(text)

    if n <= 1:
        return 0

    counts = {}

    for ch in string.ascii_uppercase:
        counts[ch] = 0

    for ch in text:
        if ch in string.ascii_uppercase:
            counts[ch] += 1

    numerator = 0

    for count in counts.values():
        numerator += count * (count - 1)

    denominator = n * (n - 1)

    return numerator / denominator

def split_into_groups(ciphertext, key_length):
    groups = []

    for i in range(key_length):
        group = ciphertext[i::key_length]
        groups.append(group)

    return groups

def frequency_analysis(group):
    frequencies = {}

    for letter in string.ascii_uppercase:
        frequencies[letter] = 0

    for ch in group:
        if ch in string.ascii_uppercase:
            frequencies[ch] += 1

    result = list(frequencies.items())
    result.sort(key=lambda x: x[1], reverse=True)

    return result

def find_shift(group):
    english_frequency = [
        8.17, 1.49, 2.78, 4.25, 12.70, 2.23,
        2.02, 6.09, 6.97, 0.15, 0.77, 4.03,
        2.41, 6.75, 7.51, 1.93, 0.10, 5.99,
        6.33, 9.06, 2.76, 0.98, 2.36, 0.15,
        1.97, 0.07
    ]

    best_shift = 0
    best_score = float("inf")

    for shift in range(26):
        counts = [0] * 26

        for ch in group:
            encrypted_value = ord(ch) - ord("A")
            plain_value = (encrypted_value - shift) % 26
            counts[plain_value] += 1

        total = len(group)
        score = 0

        for i in range(26):
            expected = english_frequency[i] * total / 100
            observed = counts[i]

            if expected > 0:
                score += ((observed - expected) ** 2) / expected

        if score < best_score:
            best_score = score
            best_shift = shift

    return best_shift

def find_key(groups):
    key = ""

    for group in groups:
        shift = find_shift(group)
        letter = chr(ord("A") + shift)
        key += letter

    return key

def vigenere_encrypt(plaintext, key):
    ciphertext = ""

    for i, ch in enumerate(plaintext):
        plain_value = ord(ch) - ord("A")
        key_value = ord(key[i % len(key)]) - ord("A")

        cipher_value = (plain_value + key_value) % 26

        ciphertext += chr(ord("A") + cipher_value)

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""

    for i, ch in enumerate(ciphertext):
        cipher_value = ord(ch) - ord("A")
        key_value = ord(key[i % len(key)]) - ord("A")

        plain_value = (cipher_value - key_value) % 26

        plaintext += chr(ord("A") + plain_value)

    return plaintext

def verify(original_ciphertext, plaintext, key):
    generated_ciphertext = vigenere_encrypt(plaintext, key)

    return generated_ciphertext == original_ciphertext

if __name__ == "__main__":
    with open("datasets/vigenere_ciphertext.txt", "r", encoding="utf-8") as file:
        ciphertext = file.read()

    ciphertext = clean_ciphertext(ciphertext)

    print("Cleaned length:", len(ciphertext))

    kasiski_results = kasiski_analysis(ciphertext)

    print("\nKasiski Analysis:")
    print("Key Length   Occurrences")

    for key_length, count in kasiski_results:
        print(f"{key_length:10}   {count}")

    print("\nIC Analysis:")
    print("Key Length   Average IC")

    for key_length in range(2, 21):
        groups = split_into_groups(ciphertext, key_length)

        total_ic = 0

        for group in groups:
            total_ic += calculate_ic(group)

        average_ic = total_ic / key_length

        print(f"{key_length:10}   {average_ic:.4f}")

    key_length = 12

    groups = split_into_groups(ciphertext, key_length)

    print("\n" + "=" * 60)
print("PROBABLE SHIFTS")
print("=" * 60)

shifts = []

for i, group in enumerate(groups, start=1):
    shift = find_shift(group)
    shifts.append(shift)

    letter = chr(ord("A") + shift)

    print(
        f"Group {i:2} -> Shift: {shift:2} -> Key letter: {letter}"
    )

    key = find_key(groups)

print("\n" + "=" * 60)
print("RECOVERED KEY")
print("=" * 60)
print("Key:", key)

plaintext = vigenere_decrypt(ciphertext, key)

print("\n" + "=" * 60)
print("RECOVERED PLAINTEXT")
print("=" * 60)

print(plaintext)

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

result = verify(ciphertext, plaintext, key)

print("Original ciphertext length :", len(ciphertext))
print("Generated ciphertext length:", len(vigenere_encrypt(plaintext, key)))
print("Ciphertext matches         :", result)

if result:
    print("VERIFICATION SUCCESSFUL")
else:
    print("VERIFICATION FAILED")