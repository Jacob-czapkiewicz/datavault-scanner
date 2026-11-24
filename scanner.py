# Bring in the Path tool from Python's built-in "pathlib" library.
# A Path is an object that represents a file or folder location.
from pathlib import Path

from rules import RULES

print("DataVault v0.0")


# Build the path to the test folder, piece by piece.
# Path.home() is your home folder (/Users/jacob), and / joins the pieces.
p = Path.home() / "Programming" / "dv_security_scanner"

SKIP_DIRS = {".git", "venv", "__pycache__", "node_modules"}

def is_binary(path):
    """Return True if the file at path is binary, False if it's text."""
    with open(path, "rb") as f:
        chunk = f.read(1024)  # read the first 1 KB of the file
    return b"\x00" in chunk   # True if there's a null byte, False otherwise

def main():
    """Main function to scan files in the dv_security_scanner folder."""
    count = 0
    for item in p.rglob("*"):
        if not item.is_file():
            continue  # Skip directories, only count files
        if any(part in SKIP_DIRS for part in item.parts):
            continue  # Skip files inside .git, venv, __pycache__ or node_modules
        if item.stat().st_size > 1024 * 1024:
            continue  # Skip files larger than 1 MB
            
        try:
            if is_binary(item):
                continue  # Skip binary files
            with open(item, "r", encoding="utf-8", errors="ignore") as f:
                for line_num, line in enumerate(f, start=1):
                    for rule in RULES:
                        for r in rule["pattern"].finditer(line):
                            print(f"[{rule['severity']}] {rule['name']} found in {item}:{line_num}")
                            
                                
            count += 1
        except OSError as e:
            print(f"Error occurred while processing {item}: {e}")



    print(f"Total files scanned: {count}")







if __name__ == "__main__":
    main()
    