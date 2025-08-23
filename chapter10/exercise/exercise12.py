from pathlib import Path
import json

path = Path("chapter10/exercise/favorite_num2.json")

if path.exists():
    contents = path.read_text(encoding="utf-8")
    print(json.loads(contents))
else:
    favorite_number = int(input("당신이 좋아하는 숫자는? "))
    path.write_text(json.dumps(favorite_number))
