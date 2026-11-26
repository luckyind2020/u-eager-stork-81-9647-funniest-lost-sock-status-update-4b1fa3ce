"""Funniest Lost Sock Status Update.

Reads the single status-update line from entry.txt (kept next to this
file), validates it against the bounty gate (1-120 UTF-8 characters,
one line, not only whitespace), writes it to /output/entry.txt for the
sealed scorer, and prints it.
"""

from pathlib import Path

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def load_line() -> str:
    """Read the entry line from entry.txt beside this file."""
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8")


def validate_line(line: str) -> str:
    """Check one status-update line against the gate; return it stripped."""
    text = line.strip()
    if not text:
        raise SystemExit("entry.txt is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 120 limit")
    return text


def publish_line(line: str) -> None:
    """Write the validated line for the sealed scorer and print it."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(line)


def main() -> None:
    line = validate_line(load_line())
    publish_line(line)


if __name__ == "__main__":
    main()
