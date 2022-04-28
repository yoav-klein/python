
from pathlib import Path

# listing subdirectories
print("=== listing files in directory (iterdir)")
p = Path('.')

for entry in p.iterdir():
    print(entry)

# get current working directory
print("=== cwd")
print(Path.cwd())

print("=== home directory")
print(Path.home())

print("=== stats")
p = Path('pathlib-examples.py')
print(p.stat())

print("=== exists")
print(f"pathlib-examples.py exists:  {p.exists()}")
q = Path("kuku")
print(f"kuku doesn't:  {q.exists()}")

print("=== is_dir")
p = Path(".")
print(f"This is a directory: {p.is_dir()}")

print("=== is_file")
p = Path("pathlib-examples.py")
print(f"pathlib-examples.py is a file: {p.is_file()}")

print("=== creating directory (mkdir)")
new_dir = Path('new-dir')
new_dir.mkdir()

print("=== create the directory again, although existing ! (mkdir)")
new_dir.mkdir(exist_ok=True)

print("=== delete directory (rmdir)")
new_dir.rmdir()

print("=== open a file")
text_file = Path("text-file.txt")
with text_file.open() as f:
    print(f.readline())

#print("=== write_text to file")
#text_file.write_text("Written with write_text")

print("=== read text from file (read_text)")
print(text_file.read_text(encoding="UTF16"))

print("=== rename file")
new_name = text_file.rename("new-name.txt")
new_name.rename("text-file.txt")

print("=== resolve to absolute path")
absolute = text_file.resolve()
print(absolute)

print("=== write to file with write_text")
new_file = Path('new-text-file.txt')
new_file.write_text("Written with write_text")

print("=== now read it..")
print(new_file.read_text())