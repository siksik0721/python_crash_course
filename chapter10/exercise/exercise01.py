from pathlib import Path

path = Path("chapter10/exercise/learning_python.txt")
contents = path.read_text(encoding="UTF8").rstrip()

print(contents)

print("########")

lines = contents.splitlines()
for line in lines:
    print(line)
