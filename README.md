# CryptoLabX — Cryptanalysis Toolkit

> A modular, extensible Python-based cryptanalysis framework developed as a semester-long academic project.

---

## 📌 Project Overview

**CryptoLabX** is a command-line cryptanalysis toolkit designed to grow incrementally across weekly assignments. Starting with a solid project foundation (Week 1), the toolkit will eventually support classical and modern ciphers, cryptanalytic attacks, mathematical utilities, and text analysis tools.

This repository contains the **Week 1 Foundation** — the project structure, a menu-driven CLI, file analysis capabilities, and automated session logging.

---

## 👥 Team Members

| Name | Roll Number | Contribution |
|------|-------------|--------------|
| Member 1 | 2024UCPXXXX | Project setup, CLI development |
| Member 2 | 2024UCPXXXX | File analysis, datasets |
| Member 3 | 2024UCPXXXX | Logging, documentation |

> *Update the table above with your actual team details.*

---

## 🗂️ Folder Structure

```
CryptoLabX/
├── classical/          # Classical cipher implementations (Caesar, Vigenère, etc.)
├── attacks/            # Cryptanalysis attack modules (brute-force, frequency, etc.)
├── math/               # Mathematical utilities (modular arithmetic, primes, etc.)
├── modern/             # Modern cryptographic algorithms (AES, RSA, etc.)
├── analysis/           # Text and cipher analysis tools
├── datasets/           # Sample text files for testing and analysis
│   ├── sample1_cryptography_intro.txt
│   ├── sample2_caesar_cipher.txt
│   ├── sample3_symmetric_encryption.txt
│   ├── sample4_frequency_analysis.txt
│   └── sample5_public_key_crypto.txt
├── outputs/            # Generated output files and session logs
├── docs/               # Additional project documentation
├── tests/              # Unit tests for all modules
├── utils/              # Shared utility modules
│   ├── __init__.py
│   ├── logger.py       # Session logging with timestamps
│   └── file_analyzer.py # Text file statistical analysis
├── main.py             # Entry point — menu-driven CLI
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CryptoLabX_GroupXX.git
cd CryptoLabX_GroupXX

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

---

## 🖥️ Features (Week 1)

### Menu-Driven CLI
The application presents an interactive menu with five options:

| Option | Function | Status |
|--------|----------|--------|
| 1 | Encrypt | 🔜 Coming Soon |
| 2 | Decrypt | 🔜 Coming Soon |
| 3 | Attack | 🔜 Coming Soon |
| 4 | Analyze File | ✅ Implemented |
| 5 | Exit | ✅ Implemented |

### File Analysis (Option 4)
Reads a text file from the `datasets/` folder and displays:
- **Number of characters** — total character count including whitespace
- **Number of words** — whitespace-delimited token count
- **Number of lines** — line count in the file
- **Unique characters** — set of distinct characters found
- **Letter frequency** — percentage distribution of each letter with a visual bar chart

### Session Logging
Every menu selection is recorded in `outputs/cryptolabx.log` with:
- Date and time of action
- The menu option selected
- Session start/end markers

---

## 📊 Sample Output

```
══════════════════════════════════════════════════════════════
  FILE ANALYSIS REPORT
══════════════════════════════════════════════════════════════
  File      : sample1_cryptography_intro.txt
  Path      : C:\...\datasets\sample1_cryptography_intro.txt
──────────────────────────────────────────────────────────────
  Characters : 987
  Words      : 152
  Lines      : 15
  Unique Chars: 48
──────────────────────────────────────────────────────────────
  LETTER FREQUENCY (sorted by frequency)
  Letter    Count     Percentage  Bar
  E         82        12.45%      ████████████████████
  T         68        10.33%      ████████████████
  ...
══════════════════════════════════════════════════════════════
```

---

## 📅 Future Modules

| Week | Module | Description |
|------|--------|-------------|
| 2 | `classical/` | Caesar cipher, Vigenère cipher |
| 3 | `attacks/` | Brute-force, frequency analysis attacks |
| 4 | `math/` | Modular arithmetic, GCD, prime utilities |
| 5 | `modern/` | AES, DES implementations |
| 6 | `analysis/` | Index of Coincidence, Kasiski examination |
| 7+ | `tests/` | Comprehensive unit tests |

---

## 📝 Log File Format

Each session generates entries in `outputs/cryptolabx.log`:

```
============================================================
  CryptoLabX Session Started at 2026-08-07 22:55:00
============================================================
[2026-08-07 22:55:05]  Option Selected: Encrypt
[2026-08-07 22:55:12]  Option Selected: Analyze -> sample1_cryptography_intro.txt
[2026-08-07 22:55:20]  Option Selected: Exit
```

---

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Version Control**: Git & GitHub
- **Libraries**: Standard library only (no external dependencies required for Week 1)

---

## 📜 License

This project is developed for academic purposes as part of the Cryptography & Network Security course.

---

## 🤝 Contributing

Each team member should:
1. Create a feature branch for their work
2. Make meaningful, descriptive commits
3. Submit pull requests for code review
4. Ensure all code is tested before merging

---

*CryptoLabX — Building the future of cryptanalysis, one week at a time. 🔐*
