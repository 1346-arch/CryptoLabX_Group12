import random
import time
import os


# Generate 16-byte token
def generate_token(seed):

    r = random.Random(seed)

    token = bytes(
        [r.getrandbits(8) for i in range(16)]
    )

    return token


# Recover timestamp
def recover_timestamp(token, start, end):

    recovered_time = None
    tested = 0

    for candidate in range(start, end + 1):

        tested += 1

        generated_token = generate_token(candidate)

        if generated_token == token:
            recovered_time = candidate

    return recovered_time, tested


# Main function
def main():

    print("===== PREDICTABLE RESET TOKEN =====")

    # Generate timestamp
    T = int(time.time())

    # Generate original token
    token = generate_token(T)

    print("\nOriginal Timestamp:", T)
    print("Original Token:", token.hex())

    # Search interval
    start = T - 300
    end = T + 300

    print("\nSearch Start:", start)
    print("Search End:", end)

    # Recover timestamp
    recovered_time, tested = recover_timestamp(
        token, start, end
    )

    print("\n===== TOKEN PREDICTION =====")

    print("Candidates Tested:", tested)
    print("Recovered Timestamp:", recovered_time)

    # Verify token
    if recovered_time is not None:

        recovered_token = generate_token(recovered_time)

        print("Recovered Token:", recovered_token.hex())

        print("Timestamp Verification:", recovered_time == T)

        print("Token Verification:", recovered_token == token)

    else:
        print("Timestamp Not Found")

    # Save output
    os.makedirs("outputs/mt19937", exist_ok=True)

    with open("outputs/mt19937/reset_token_output.txt", "w") as f:

        f.write("PREDICTABLE RESET TOKEN\n")
        f.write("Original Timestamp: " + str(T) + "\n")
        f.write("Original Token: " + token.hex() + "\n")
        f.write("Search Start: " + str(start) + "\n")
        f.write("Search End: " + str(end) + "\n")
        f.write("Candidates Tested: " + str(tested) + "\n")
        f.write("Recovered Timestamp: " + str(recovered_time) + "\n")

        if recovered_time is not None:
            f.write("Recovered Token: " +
                    generate_token(recovered_time).hex() + "\n")

    print("\nOutput saved successfully!")


if __name__ == "__main__":
    main()