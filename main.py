#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — deterministic one-line entry.

Writes the excuse to /output/entry.txt, byte-identical on every run.
No input, no network, no randomness.
"""

import os
import sys

ENTRY = "Sorry \u2014 I marked your deadline stale after 14 days of inactivity and auto-closed it, then reopened it as a feature request for next quarter."

def validate_entry(entry):
    """Check the entry meets the one-line excuse format.

    Rules: 1-200 characters, exactly one line, no leading or
    trailing whitespace. Exits non-zero with a clear message
    on the first rule violated.
    """
    if not 1 <= len(entry) <= 200:
        print(f"error: ENTRY must be 1-200 characters, got {len(entry)}",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("error: ENTRY must be exactly one line", file=sys.stderr)
        sys.exit(1)
    if entry != entry.strip():
        print("error: ENTRY must not have leading or trailing whitespace",
              file=sys.stderr)
        sys.exit(1)

def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
