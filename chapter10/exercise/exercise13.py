from pathlib import Path
import json

username = input("What is your name? ")
age = input("What is your age? ")
user = {"username": username, "age": age}

path = Path("chapter10/exercise/user.json")
contents = json.dumps(user)
path.write_text(contents)

print(f"We'll remeber you when you come back, {username}!")

contents = path.read_text(encoding="utf-8")
user = json.loads(contents)

print(f"Welcome back, {user["username"]}!")
print(user)
