
import subprocess
import os

def generate_random_data(size, output_file):
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        powershell_script = f'''
        $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
        $bytes = New-Object byte[] {size}
        $rng.GetBytes($bytes)
        [System.IO.File]::WriteAllBytes("{output_file}", $bytes)
        $rng.Dispose()
        '''

        subprocess.run(
            ["powershell", "-NoProfile", "-Command", powershell_script],
            check=True
        )

        print(f"Generated {size} bytes successfully.")
        print(f"Saved to: {output_file}")

    except FileNotFoundError:
        print("PowerShell is not available. Run this on Windows.")

    except subprocess.CalledProcessError as e:
        print("Windows CNG generation failed:", e)


if __name__ == "__main__":
    generate_random_data(
        1024 * 1024,
        "os_random/outputs/windows_cng.bin"
    )
