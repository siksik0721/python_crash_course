from pathlib import Path
import json

path = Path("chapter10/exercise/favorite_num.json")
contents = path.read_text(encoding="utf-8")
print(json.loads(contents))
