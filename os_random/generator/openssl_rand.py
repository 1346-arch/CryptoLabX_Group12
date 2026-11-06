
import subprocess
import os

def generate_random_data(size, output_file):
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        subprocess.run(
            ["openssl", "rand", "-out", output_file, str(size)],
            check=True
        )

        print(f"Generated {size} bytes successfully.")
        print(f"Saved to: {output_file}")

    except FileNotFoundError:
        print("Error: OpenSSL is not installed or not in PATH.")

    except subprocess.CalledProcessError as e:
        print("OpenSSL generation failed:", e)


if __name__ == "__main__":
    generate_random_data(
        1024 * 1024,
        "os_random/outputs/openssl_rand.bin"
    )
