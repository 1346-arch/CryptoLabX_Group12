"""
logger.py - Logging utility for CryptoLabX
Records date, time, and selected menu option for every execution.
"""

import os
import datetime


class Logger:
    """Maintains a persistent log file that records every menu interaction."""

    def __init__(self, log_dir="outputs", log_filename="cryptolabx.log"):
        """
        Initialize the Logger.

        Args:
            log_dir (str): Directory where the log file is stored.
            log_filename (str): Name of the log file.
        """
        self.log_dir = log_dir
        self.log_path = os.path.join(log_dir, log_filename)

        # Ensure the output directory exists
        os.makedirs(self.log_dir, exist_ok=True)

    def log(self, menu_option):
        """
        Write a timestamped log entry for the selected menu option.

        Args:
            menu_option (str): Description of the menu option selected.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}]  Option Selected: {menu_option}\n"

        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(entry)

    def log_startup(self):
        """Record a session start marker in the log."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        separator = "=" * 60
        entry = (
            f"\n{separator}\n"
            f"  CryptoLabX Session Started at {timestamp}\n"
            f"{separator}\n"
        )

        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(entry)

    def get_log_path(self):
        """Return the absolute path to the log file."""
        return os.path.abspath(self.log_path)
