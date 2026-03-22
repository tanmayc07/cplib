from pathlib import Path
from datetime import datetime

def read_tracker(fpath):
    if not fpath.exists():
        return
    
    lines = fpath.read_text().splitlines(keepends=True)
    return lines
    
if __name__ == "__main__":
    path = Path("tracker.md")
    
    data = read_tracker(path)
    if data:
        date_now = datetime.now().strftime('%b %d')
        for line in data:
            if date_now in line:
                split_line = line.split('|')
                print(
                    f"{split_line[2].strip()}_{split_line[4].strip()} {split_line[3].strip()}\n"
                    f"First Solved: {split_line[1]}\n"
                    f"Note:\n"
                    f"{split_line[5].strip()}\n"
                )
    