from pathlib import Path


def main():
    line = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    print(line)


if __name__ == "__main__":
    main()
