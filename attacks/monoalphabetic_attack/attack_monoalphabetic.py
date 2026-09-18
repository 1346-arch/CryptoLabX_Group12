from monoalphabetic_attack import (
    display_partial_plaintext,
    apply_substitution,
    verify_solution
)

ciphertext_file = "outputs/monoalphabetic/ciphertext.txt"

with open(ciphertext_file, "r", encoding="utf-8") as file:
    ciphertext = file.read()


# ---------------------------------------------------------
# Store substitutions
# ---------------------------------------------------------

substitutions = {}


# ---------------------------------------------------------
# Record cryptanalysis decisions
# ---------------------------------------------------------

decisions = []


def record_decision(step, observation, candidate,
                    tested, result, decision):

    decisions.append({
        "step": step,
        "observation": observation,
        "candidate": candidate,
        "tested": tested,
        "result": result,
        "decision": decision
    })


# ---------------------------------------------------------
# Test a substitution
# ---------------------------------------------------------

def test_substitution(step, observation, candidate,
                      cipher_letter, plain_letter):

    substitutions[cipher_letter] = plain_letter

    plaintext = apply_substitution(
        ciphertext,
        substitutions
    )

    record_decision(
        step,
        observation,
        candidate,
        cipher_letter + " -> " + plain_letter,
        "Partial plaintext examined.",
        "Keep"
    )

    return plaintext


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

print("=" * 70)
print("MONOALPHABETIC CIPHER - ITERATIVE CRYPTANALYSIS")
print("=" * 70)


# =========================================================
# STEP 1
# ZIT -> THE
# =========================================================

test_substitution(
    1,
    "ZIT occurs frequently and is a common three-letter word.",
    "ZIT -> THE",
    "Z",
    "T"
)

substitutions["I"] = "H"
substitutions["T"] = "E"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 2
# ZG -> TO
# =========================================================

test_substitution(
    2,
    "ZG occurs frequently and becomes T_ after Z -> T.",
    "ZG -> TO",
    "G",
    "O"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 3
# O -> I
# =========================================================

test_substitution(
    3,
    "O is a one-letter word and O -> I creates readable text.",
    "O -> I",
    "O",
    "I"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 4
# O -> A REJECTED
# =========================================================

record_decision(
    4,
    "O is a one-letter word, so A was considered.",
    "O -> A",
    "O -> A",
    "Produced less meaningful plaintext.",
    "Reject"
)

substitutions["O"] = "I"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 5
# INTRODUCTION
#
# OFZKGRXEZOGF -> INTRODUCTION
# =========================================================

test_substitution(
    5,
    "OFZKGRXEZOGF matches the beginning of INTRODUCTION.",
    "OFZKGRXEZOGF -> INTRODUCTION",
    "F",
    "N"
)

substitutions["K"] = "R"
substitutions["R"] = "D"
substitutions["X"] = "U"
substitutions["E"] = "C"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 6
# MODERN
#
# DGRTKF -> MODERN
# =========================================================

test_substitution(
    6,
    "DGRTKF has the partial pattern _ODER_.",
    "DGRTKF -> MODERN",
    "D",
    "M"
)

substitutions["F"] = "N"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 7
# CRYPTOGRAPHY
#
# EKNHZGUKQHIN -> CRYPTOGRAPHY
# =========================================================

test_substitution(
    7,
    "EKNHZGUKQHIN matches the pattern of CRYPTOGRAPHY.",
    "EKNHZGUKQHIN -> CRYPTOGRAPHY",
    "N",
    "Y"
)

substitutions["H"] = "P"
substitutions["U"] = "G"
substitutions["Q"] = "A"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 8
# ALPHABET
#
# QSHIQWTZ -> ALPHABET
# =========================================================

test_substitution(
    8,
    "QSHIQWTZ becomes A_PHA_ET.",
    "QSHIQWTZ -> ALPHABET",
    "S",
    "L"
)

substitutions["W"] = "B"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 9
# KEY
#
# ATN -> KEY
# =========================================================

test_substitution(
    9,
    "ATN becomes _EY.",
    "ATN -> KEY",
    "A",
    "K"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 10
# HOW
#
# IGV -> HOW
# =========================================================

test_substitution(
    10,
    "IGV becomes HO_ and appears in 'Show how to'.",
    "IGV -> HOW",
    "V",
    "W"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 11
# KASISKI
#
# AQLOLAO -> KASISKI
# =========================================================

test_substitution(
    11,
    "AQLOLAO becomes KA_I_KI with the known mappings.",
    "AQLOLAO -> KASISKI",
    "L",
    "S"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 12
# CONFIRMATION WORDS
#
# QFR -> AND
# YGK -> FOR
# WKTQA -> BREAK
# =========================================================

record_decision(
    12,
    "QFR becomes AND with the recovered mappings.",
    "QFR -> AND",
    "Q -> A, F -> N, R -> D",
    "Readable word AND.",
    "Keep"
)

record_decision(
    12,
    "YGK becomes FOR with the recovered mappings.",
    "YGK -> FOR",
    "Y -> F, G -> O, K -> R",
    "Readable word FOR.",
    "Keep"
)

record_decision(
    12,
    "WKTQA becomes BREAK with the recovered mappings.",
    "WKTQA -> BREAK",
    "W -> B, K -> R, T -> E, Q -> A, A -> K",
    "Readable word BREAK.",
    "Keep"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 13
# CONTEXT CONFIRMATION
# =========================================================

record_decision(
    13,
    "Repeated words and readable context confirm the recovered mappings.",
    "Previously recovered substitutions",
    "Existing substitutions",
    "Plaintext becomes readable.",
    "Keep"
)

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# STEP 14
# REMAINING MAPPINGS
# =========================================================

test_substitution(
    14,
    "The remaining ciphertext letters are identified from "
    "repeated patterns and readable plaintext context.",
    "Remaining mappings complete the substitution alphabet.",
    "B",
    "X"
)

substitutions["C"] = "V"
substitutions["J"] = "Q"
substitutions["M"] = "Z"
substitutions["P"] = "J"
substitutions["Y"] = "F"

display_partial_plaintext(
    ciphertext,
    substitutions
)


# =========================================================
# RECOVERED SUBSTITUTIONS
# =========================================================

print("\n" + "=" * 70)
print("RECOVERED SUBSTITUTIONS")
print("=" * 70)

for cipher in sorted(substitutions):
    print(
        cipher,
        "->",
        substitutions[cipher]
    )


# =========================================================
# FINAL PARTIAL PLAINTEXT
# =========================================================

print("\n" + "=" * 70)
print("FINAL PARTIAL PLAINTEXT")
print("=" * 70)

recovered_plaintext = apply_substitution(
    ciphertext,
    substitutions
)

print(recovered_plaintext)


# =========================================================
# CRYPTANALYTIC DECISIONS
# =========================================================

print("\n" + "=" * 70)
print("CRYPTANALYTIC DECISIONS")
print("=" * 70)

print(
    "Step | Observation | Possible Substitution | "
    "Substitution Tested | Result | Decision"
)

print("-" * 70)

for item in decisions:

    print(
        item["step"], "|",
        item["observation"], "|",
        item["candidate"], "|",
        item["tested"], "|",
        item["result"], "|",
        item["decision"]
    )


# =========================================================
# FINAL VERIFICATION
# =========================================================

print("\n" + "=" * 70)
print("FINAL VERIFICATION")
print("=" * 70)


# ---------------------------------------------------------
# Check missing mappings
# ---------------------------------------------------------

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

missing = []

for letter in alphabet:

    if letter not in substitutions:
        missing.append(letter)

print(
    "Missing mappings:",
    missing
)


# ---------------------------------------------------------
# Check duplicate plaintext mappings
# ---------------------------------------------------------

plaintext_letters = list(
    substitutions.values()
)

duplicates = []

for letter in plaintext_letters:

    if plaintext_letters.count(letter) > 1:

        if letter not in duplicates:
            duplicates.append(letter)

print(
    "Duplicate plaintext mappings:",
    duplicates
)


# ---------------------------------------------------------
# Create reverse mapping
# ---------------------------------------------------------

reverse = {}

for cipher_letter in substitutions:

    plain_letter = substitutions[cipher_letter]

    reverse[plain_letter] = cipher_letter


# ---------------------------------------------------------
# Re-encrypt recovered plaintext
# ---------------------------------------------------------

generated_ciphertext = ""

for ch in recovered_plaintext:

    if ch.upper() in alphabet:

        plain_letter = ch.upper()

        if plain_letter in reverse:

            new_ch = reverse[plain_letter]

            if ch.islower():
                new_ch = new_ch.lower()

            generated_ciphertext += new_ch

        else:

            generated_ciphertext += ch

    else:

        generated_ciphertext += ch


# ---------------------------------------------------------
# Compare original and generated ciphertext
# ---------------------------------------------------------

print(
    "Ciphertext matches:",
    generated_ciphertext == ciphertext
)


# =========================================================
# FINAL RESULT
# =========================================================

if (
    len(missing) == 0
    and len(duplicates) == 0
    and generated_ciphertext == ciphertext
):

    print("\n" + "=" * 70)
    print("CRYPTANALYSIS SUCCESSFUL")
    print("=" * 70)

else:

    print("\n" + "=" * 70)
    print("CRYPTANALYSIS NEEDS CORRECTION")
    print("=" * 70)