from pathlib import Path

names = ""
while True:
    name = input("사용자 이름이 무엇입니까? (종료하려면 'quit'을 입력하세요) ")

    if name == "quit":
        break

    names += name + "\n"

path = Path("chapter10/exercise/guest_book.txt")
path.write_text(names, encoding="UTF8")
