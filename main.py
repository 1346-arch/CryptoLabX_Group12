"""
main.py - CryptoLabX Command-Line Interface
============================================
Entry point for the CryptoLabX cryptanalysis toolkit.
Provides a menu-driven interface for Encrypt, Decrypt, Attack,
Analyze, and Exit operations.

Usage:
    python main.py
"""

import os
import sys

# Ensure project root is on the import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.logger import Logger
from utils.file_analyzer import FileAnalyzer


# ──────────────────────────────────────────────
#  ANSI colour helpers (work on Windows 10+)
# ──────────────────────────────────────────────
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RESET   = "\033[0m"


def enable_windows_ansi():
    """Enable ANSI escape sequences on Windows 10+ terminals."""
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass


def print_banner():
    """Display the CryptoLabX welcome banner."""
    banner = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║       ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ║
║      ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗║
║      ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║║
║      ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║║
║      ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝║
║       ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ║
║                  {YELLOW}L A B X  ·  T O O L K I T{CYAN}                ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║  {GREEN}Cryptanalysis Framework{CYAN}        {DIM}v1.0 · Week 1 Foundation{CYAN}{BOLD}  ║
╚══════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)


def print_menu():
    """Display the main menu options."""
    print(f"""
{BOLD}{CYAN}┌──────────────────────────────────────┐
│         {YELLOW}★  MAIN MENU  ★{CYAN}               │
├──────────────────────────────────────┤
│                                      │
│   {GREEN}[1]{CYAN}  Encrypt                        │
│   {GREEN}[2]{CYAN}  Decrypt                        │
│   {GREEN}[3]{CYAN}  Attack                         │
│   {GREEN}[4]{CYAN}  Analyze File                   │
│   {GREEN}[5]{CYAN}  Exit                           │
│                                      │
└──────────────────────────────────────┘{RESET}
""")


def coming_soon(feature_name):
    """Display a 'Coming Soon' message for unimplemented features."""
    print(f"""
{YELLOW}  ┌────────────────────────────────────────┐
  │  ⏳  {BOLD}{feature_name}{RESET}{YELLOW} — Coming Soon!          │
  │                                        │
  │  This module will be available in a     │
  │  future assignment. Stay tuned!         │
  └────────────────────────────────────────┘{RESET}
""")


def handle_analyze(analyzer, logger):
    """
    Handle the Analyze File menu option.
    Lists available dataset files and lets the user select one for analysis.
    """
    files = analyzer.list_files()

    if not files:
        print(f"\n{RED}  ✗ No .txt files found in the datasets/ folder.{RESET}")
        return

    print(f"\n{BOLD}{CYAN}  ┌─────────────────────────────────────────┐")
    print(f"  │       {YELLOW}📂  Available Dataset Files{CYAN}        │")
    print(f"  ├─────────────────────────────────────────┤{RESET}")
    for i, fname in enumerate(files, 1):
        print(f"{CYAN}  │   {GREEN}[{i}]{CYAN}  {fname:<35}│{RESET}")
    print(f"{CYAN}  │   {GREEN}[0]{CYAN}  {'Back to Main Menu':<35}│")
    print(f"  └─────────────────────────────────────────┘{RESET}")

    try:
        choice = input(f"\n{BOLD}  Select a file (0-{len(files)}): {RESET}").strip()
        choice = int(choice)
    except (ValueError, EOFError):
        print(f"\n{RED}  ✗ Invalid selection.{RESET}")
        return

    if choice == 0:
        return

    if choice < 1 or choice > len(files):
        print(f"\n{RED}  ✗ Invalid selection. Please choose 1-{len(files)}.{RESET}")
        return

    selected_file = files[choice - 1]
    logger.log(f"Analyze -> {selected_file}")

    try:
        results = analyzer.analyze(selected_file)
        formatted = FileAnalyzer.format_results(results)
        print(f"{GREEN}{formatted}{RESET}")
    except FileNotFoundError as e:
        print(f"\n{RED}  ✗ {e}{RESET}")
    except Exception as e:
        print(f"\n{RED}  ✗ An error occurred during analysis: {e}{RESET}")


def main():
    """Main application loop for CryptoLabX."""
    enable_windows_ansi()

    # Initialize utilities
    logger = Logger(log_dir="outputs")
    analyzer = FileAnalyzer(datasets_dir="datasets")

    # Log session start
    logger.log_startup()

    # Display welcome banner
    print_banner()

    while True:
        print_menu()

        try:
            choice = input(f"{BOLD}  Enter your choice (1-5): {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n{CYAN}  Goodbye! 👋{RESET}\n")
            logger.log("Exit (keyboard interrupt)")
            break

        if choice == "1":
            logger.log("Encrypt")
            coming_soon("Encrypt")

        elif choice == "2":
            logger.log("Decrypt")
            coming_soon("Decrypt")

        elif choice == "3":
            logger.log("Attack")
            coming_soon("Attack")

        elif choice == "4":
            logger.log("Analyze")
            handle_analyze(analyzer, logger)

        elif choice == "5":
            logger.log("Exit")
            print(f"""
{CYAN}{BOLD}  ┌────────────────────────────────────────┐
  │                                        │
  │   Thank you for using CryptoLabX! 🔐   │
  │   Log saved to: outputs/cryptolabx.log │
  │                                        │
  └────────────────────────────────────────┘{RESET}
""")
            break

        else:
            print(f"\n{RED}  ✗ Invalid choice. Please enter a number from 1 to 5.{RESET}")


if __name__ == "__main__":
    main()
