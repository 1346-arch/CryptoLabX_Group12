from monoalphabetic_attack import (
    frequency_analysis,
    word_frequency_analysis,
    pattern_analysis
)


ciphertext_file = "outputs/monoalphabetic/ciphertext.txt"

with open(ciphertext_file, "r", encoding="utf-8") as file:
    ciphertext = file.read()


print("=" * 60)
print("LETTER FREQUENCY ANALYSIS")
print("=" * 60)

frequency = frequency_analysis(ciphertext)

print("Letter   Count   Percentage")

for letter, count, percentage in frequency:
    if count > 0:
        print(f"{letter:>6}   {count:>5}   {percentage:>8.2f}%")


print("\n" + "=" * 60)
print("WORD FREQUENCY ANALYSIS")
print("=" * 60)

words = word_frequency_analysis(ciphertext)

for word, count in words:
    print(f"{word:20} {count}")


print("\n" + "=" * 60)
print("ONE-LETTER WORDS")
print("=" * 60)

for word, count in words:
    if len(word) == 1:
        print(word, "->", count)


print("\n" + "=" * 60)
print("TWO-LETTER WORDS")
print("=" * 60)

for word, count in words:
    if len(word) == 2:
        print(word, "->", count)


print("\n" + "=" * 60)
print("THREE-LETTER WORDS")
print("=" * 60)

for word, count in words:
    if len(word) == 3:
        print(word, "->", count)


print("\n" + "=" * 60)
print("REPEATED WORDS")
print("=" * 60)

for word, count in words:
    if count > 1:
        print(word, "->", count)


print("\n" + "=" * 60)
print("WORD PATTERNS")
print("=" * 60)

patterns = pattern_analysis(ciphertext)

for word, count, pattern in patterns:
    print(f"{word:20} {count:>3}   {pattern}")