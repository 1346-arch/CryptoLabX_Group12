
import os

def generate_random_data(size, output_file):
    try:
        with open("/dev/urandom", "rb") as random_source:
            data = random_source.read(size)

        with open(output_file, "wb") as file:
            file.write(data)

        print(f"Generated {len(data)} bytes successfully.")
        print(f"Saved to: {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    generate_random_data(
        1024 * 1024,
        "os_random/outputs/linux_urandom.bin"
    )
