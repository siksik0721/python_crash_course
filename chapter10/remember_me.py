from pathlib import Path
import json

username = input("What is your name? ")

path = Path("chapter10/username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remeber you when you come back, {username}!")
