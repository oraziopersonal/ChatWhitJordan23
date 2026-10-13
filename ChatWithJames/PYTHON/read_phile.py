from pathlib import Path

file_path = Path(__file__).with_name("brain.txt")

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
