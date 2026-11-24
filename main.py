import sys
from pathlib import Path


def main():
    script = Path(__file__)
    entry = script.with_name("entry.txt")
    try:
        line = entry.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print(f"error: {entry.name} not found next to {script.name}", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
