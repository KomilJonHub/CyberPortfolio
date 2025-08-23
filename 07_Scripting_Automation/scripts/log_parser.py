#!/usr/bin/env python3
"""Simple log parser to count error entries."""
import sys


def parse_log(path: str) -> int:
    """Return the number of lines containing the word 'ERROR'."""
    errors = 0
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            if "ERROR" in line:
                errors += 1
    return errors


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: log_parser.py <logfile>")
        raise SystemExit(1)

    logfile = sys.argv[1]
    count = parse_log(logfile)
    print(f"{count} error entries found in {logfile}")


if __name__ == "__main__":
    main()
