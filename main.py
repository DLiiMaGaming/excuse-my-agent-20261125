#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — deterministic one-line entry.

Writes the excuse to /output/entry.txt, byte-identical on every run.
No input, no network, no randomness.
"""

import os

ENTRY = "Sorry \u2014 I marked your deadline stale after 14 days of inactivity and auto-closed it, then reopened it as a feature request for next quarter."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
