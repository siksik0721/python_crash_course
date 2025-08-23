from pathlib import Path

path = Path("chapter10/exercise/learning_python.txt")
contents = path.read_text(encoding="UTF8").rstrip()

contents = contents.replace("파이썬", "C++")
contents = contents.replace("Python", "C++")
print(contents)
