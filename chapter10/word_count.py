from pathlib import Path


def count_words(path):
    """파일에 포함된 단어개수를 대략적으로 셉니다"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 파일에 포함된 단어 개수를 대략적으로 셉니다
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ["alice.txt", "siddharta.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    path = Path(f"chapter10/{filename}")
    count_words(path)
