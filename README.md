# CryptoLabX

CryptoLabX is a semester-long, modular cryptanalysis toolkit developed for the Week 1 foundation assignment. This first version establishes the project layout, a command-line foundation, reusable datasets, file handling, logging, and basic text analysis. It deliberately does **not** implement encryption, decryption, or attack algorithms yet.

## Team members

| Name | Student ID | Contribution |
| --- | --- | --- |
| Shivam Pareek | 2024UCP1346 | Project coordination, CLI, file analysis, logging & documentation |

*(Add other team members here if applicable)*

## Project structure

```text
CryptoLabX/
├── classical/       # Future classical ciphers (Caesar, Vigenere, etc.)
├── attacks/         # Future cryptanalytic attack implementations
├── math/            # Number-theory and mathematical helper functions
├── modern/          # Future modern cryptography modules
├── analysis/        # File and frequency-analysis utilities
├── datasets/        # Plain-text samples used for testing and analysis
│   ├── sample1_cryptography_intro.txt
│   ├── sample2_caesar_cipher.txt
│   ├── sample3_symmetric_encryption.txt
│   ├── sample4_frequency_analysis.txt
│   └── sample5_public_key_crypto.txt
├── outputs/         # Generated analysis results and future reports (cryptolabx.log)
├── docs/            # Project documentation
├── tests/           # Automated unit tests
├── utils/           # Shared helpers (logger.py, file_analyzer.py)
├── main.py          # Menu-driven application entry point
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

## Week 1 functionality

The main program presents options for **Encrypt**, **Decrypt**, **Attack**, **Analyze**, and **Exit**. The first three options display a "Coming Soon" notification.

Option 4 (**Analyze**) lists all files in the `datasets/` folder, lets the user select a file, and calculates:
- Character count
- Word count
- Line count
- Unique character set and count
- Letter frequency analysis (sorted by frequency with visual bar visualization)

Every user interaction and menu selection is automatically recorded with timestamps in `outputs/cryptolabx.log`.

## Setup and Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/1346-arch/CryptoLabX_Group12.git
   cd CryptoLabX_Group12
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the toolkit:**
   ```bash
   python main.py
   ```

## Sample Output

```text
==============================================================
  FILE ANALYSIS REPORT
==============================================================
  File      : sample1_cryptography_intro.txt
  Path      : .../datasets/sample1_cryptography_intro.txt
--------------------------------------------------------------
  Characters : 1171
  Words      : 172
  Lines      : 17
  Unique Chars: 48
--------------------------------------------------------------
  LETTER FREQUENCY (sorted by frequency)
  Letter    Count     Percentage  Bar
  ----------------------------------------------------
  E         113        11.69%     ████████████████████
  A         79          8.17%     █████████████
  N         79          8.17%     █████████████
...
==============================================================
```

## Future Roadmap

- **Week 2:** Classical ciphers (Caesar, Vigenère, Playfair, Hill)
- **Week 3:** Cryptanalytic attacks (Brute-force, Known-plaintext, Frequency attack)
- **Week 4:** Mathematical utilities (Modular arithmetic, GCD, Primes, Matrix algebra)
- **Week 5:** Modern ciphers (AES, DES, RSA, Diffie-Hellman)
