from pathlib import Path

path = Path("chapter10/alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # 파일에 포함된 단어 개수를 대략적으로 셉니다
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
