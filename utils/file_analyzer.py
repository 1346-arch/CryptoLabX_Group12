"""
file_analyzer.py - File analysis utility for CryptoLabX
Reads text files and computes: character count, word count, line count,
unique characters, and letter frequency distribution.
"""

import os
import string


class FileAnalyzer:
    """Analyzes text files for statistical properties useful in cryptanalysis."""

    def __init__(self, datasets_dir="datasets"):
        """
        Initialize the FileAnalyzer.

        Args:
            datasets_dir (str): Path to the directory containing text files.
        """
        self.datasets_dir = datasets_dir

    def list_files(self):
        """
        List all .txt files available in the datasets directory.

        Returns:
            list: Sorted list of .txt filenames.
        """
        if not os.path.isdir(self.datasets_dir):
            return []

        files = [
            f for f in os.listdir(self.datasets_dir)
            if f.endswith(".txt") and os.path.isfile(
                os.path.join(self.datasets_dir, f)
            )
        ]
        return sorted(files)

    def analyze(self, filename):
        """
        Perform a complete analysis of a text file.

        Args:
            filename (str): Name of the file inside the datasets directory.

        Returns:
            dict: Analysis results containing character count, word count,
                  line count, unique characters, and letter frequency.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        filepath = os.path.join(self.datasets_dir, filename)

        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        results = {
            "filename": filename,
            "filepath": os.path.abspath(filepath),
            "num_characters": len(content),
            "num_words": len(content.split()),
            "num_lines": content.count("\n") + (1 if content and not content.endswith("\n") else 0),
            "unique_characters": sorted(set(content)),
            "num_unique_characters": len(set(content)),
            "letter_frequency": self._compute_letter_frequency(content),
        }

        return results

    def _compute_letter_frequency(self, text):
        """
        Compute the frequency of each letter (case-insensitive).

        Args:
            text (str): The input text.

        Returns:
            dict: Letter -> (count, percentage) mapping, sorted by frequency descending.
        """
        text_lower = text.lower()
        total_letters = sum(1 for ch in text_lower if ch in string.ascii_lowercase)

        if total_letters == 0:
            return {}

        freq = {}
        for ch in string.ascii_lowercase:
            count = text_lower.count(ch)
            if count > 0:
                percentage = (count / total_letters) * 100
                freq[ch] = {"count": count, "percentage": round(percentage, 2)}

        # Sort by count descending
        freq = dict(
            sorted(freq.items(), key=lambda item: item[1]["count"], reverse=True)
        )

        return freq

    @staticmethod
    def format_results(results):
        """
        Format analysis results into a readable string for display.

        Args:
            results (dict): The analysis results dictionary.

        Returns:
            str: Formatted string ready for terminal output.
        """
        lines = []
        lines.append("")
        lines.append("=" * 62)
        lines.append(f"  FILE ANALYSIS REPORT")
        lines.append("=" * 62)
        lines.append(f"  File      : {results['filename']}")
        lines.append(f"  Path      : {results['filepath']}")
        lines.append("-" * 62)
        lines.append(f"  Characters : {results['num_characters']}")
        lines.append(f"  Words      : {results['num_words']}")
        lines.append(f"  Lines      : {results['num_lines']}")
        lines.append(f"  Unique Chars: {results['num_unique_characters']}")
        lines.append("-" * 62)

        # Display unique characters
        unique_display = ""
        for i, ch in enumerate(results["unique_characters"]):
            if ch == "\n":
                unique_display += "\\n "
            elif ch == "\t":
                unique_display += "\\t "
            elif ch == " ":
                unique_display += "[space] "
            else:
                unique_display += f"{ch} "
        lines.append(f"  Unique Characters:")
        lines.append(f"  {unique_display.strip()}")
        lines.append("-" * 62)

        # Display letter frequency table
        lines.append(f"  LETTER FREQUENCY (sorted by frequency)")
        lines.append(f"  {'Letter':<10}{'Count':<10}{'Percentage':<12}{'Bar'}")
        lines.append(f"  {'-'*10}{'-'*10}{'-'*12}{'-'*20}")

        freq = results["letter_frequency"]
        if freq:
            max_count = max(item["count"] for item in freq.values())
        else:
            max_count = 1

        for letter, data in freq.items():
            bar_len = int((data["count"] / max_count) * 20)
            bar = "█" * bar_len
            lines.append(
                f"  {letter.upper():<10}{data['count']:<10}{data['percentage']:>6.2f}%     {bar}"
            )

        lines.append("=" * 62)
        return "\n".join(lines)
