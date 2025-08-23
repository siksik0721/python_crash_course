from pathlib import Path
import json

path = Path("chapter10/username.json")
contents = path.read_text(encoding="utf-8")
username = json.loads(contents)

print(f"Welcome back, {username}!")
