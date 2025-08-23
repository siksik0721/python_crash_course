from pathlib import Path

path = Path("chapter10/exercise/learning_python.txt")
contents = path.read_text(encoding="UTF8").rstrip()

for line in contents.splitlines():
    print(line)
