from pathlib import Path
import json


def get_stored_username(path):
    """저장된 사용자 이름이 있으면 가져옵니다"""
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """사용자 이름을 묻습니다"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """사용자를 이름으로 환영합니다"""
    path = Path("chapter10/username.json")
    username = get_stored_username(path)
    if username:
        check = input(f"Is {username} right? (y / n): ")
        if check == "y":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remeber you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remeber you when you come back, {username}!")


greet_user()
