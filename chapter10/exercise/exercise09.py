from pathlib import Path

cats_path = Path("chapter10/exercise/cat.txt")
dogs_path = Path("chapter10/exercise/dog.txt")

try:
    print(cats_path.read_text(encoding="utf-8"))
except FileNotFoundError:
    pass

try:
    print(dogs_path.read_text(encoding="utf-8"))
except FileNotFoundError:
    pass
