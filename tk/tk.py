import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="TK",
        description="CLI tool for cplib",
    )
    
    parser.add_argument('-t', '--tracker')
    args = parser.parse_args()

    path = Path('/Users/tanmay/oss/cplib') / args.tracker
    if path.exists():
        lines = path.read_text().splitlines(keepends=True)
        print(lines[2:])