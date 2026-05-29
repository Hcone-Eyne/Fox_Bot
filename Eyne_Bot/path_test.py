from pathlib import Path 

master_path = Path(__file__).resolve().parent

all_txt = master_path.rglob("*.txt")

for f in all_txt:
    folder = f.parent.name

    print(f"Folder Name: {f} and inside the folder {folder}")

    content = f.read_text().splitlines()
    if content:
        print(f"1st line: {content[0]}")