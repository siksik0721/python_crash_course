from pathlib import Path

cats_path = Path("chapter10/exercise/cats.txt")
dogs_path = Path("chapter10/exercise/dogs.txt")

try:
    print(cats_path.read_text(encoding="utf-8"))
    print(dogs_path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("파일이 없습니다.")
