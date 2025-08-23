from pathlib import Path

name = input("사용자 이름이 무엇입니까? ")

path = Path("chapter10/exercise/guest.txt")
path.write_text(name, encoding="UTF8")
