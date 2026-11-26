"""Print the competition entry line from entry.txt, byte for byte, adding nothing."""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
