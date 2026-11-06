import random
import string
import secrets
import os


# Generate keystream and perform XOR
def encrypt_decrypt(data, seed):

    r = random.Random(seed)
    result = bytearray()

    for byte in data:
        key = r.getrandbits(8)
        result.append(byte ^ key)

    return bytes(result)


# Generate plaintext
def generate_plaintext():

    length = random.randint(5, 20)

    prefix = ''.join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )

    return (prefix + "A" * 14).encode()


# Recover seed using brute force
def recover_seed(ciphertext):

    known_text = b"A" * 14

    for seed in range(65536):

        decrypted = encrypt_decrypt(ciphertext, seed)

        if known_text in decrypted:
            return seed, decrypted

    return None, None


# Main function
def main():

    print("===== MT19937 STREAM CIPHER =====")

    plaintext = generate_plaintext()

    seed = secrets.randbelow(65536)

    ciphertext = encrypt_decrypt(plaintext, seed)

    decrypted = encrypt_decrypt(ciphertext, seed)

    print("\nOriginal Plaintext:", plaintext.decode())
    print("Original Seed:", seed)
    print("Ciphertext (Hex):", ciphertext.hex())
    print("Decrypted Plaintext:", decrypted.decode())

    print("\n===== SEED RECOVERY =====")

    recovered_seed, recovered_plaintext = recover_seed(ciphertext)

    print("Recovered Seed:", recovered_seed)

    if recovered_seed is not None:

        print("Recovered Plaintext:", recovered_plaintext.decode())

        print("Seed Verification:", recovered_seed == seed)

        print("Full Plaintext Verification:",
              recovered_plaintext == plaintext)

        print("Known Plaintext Verification:",
              b"A" * 14 in recovered_plaintext)

    else:
        print("Seed Not Found")

    # Save output
    os.makedirs("outputs/mt19937", exist_ok=True)

    with open("outputs/mt19937/stream_cipher_output.txt", "w") as f:

        f.write("MT19937 STREAM CIPHER\n")
        f.write("Original Plaintext: " + plaintext.decode() + "\n")
        f.write("Original Seed: " + str(seed) + "\n")
        f.write("Ciphertext: " + ciphertext.hex() + "\n")
        f.write("Decrypted Plaintext: " + decrypted.decode() + "\n")
        f.write("Recovered Seed: " + str(recovered_seed) + "\n")
        f.write("Recovered Plaintext: " +
                recovered_plaintext.decode() + "\n")

    print("\nOutput saved successfully!")


if __name__ == "__main__":
    main()