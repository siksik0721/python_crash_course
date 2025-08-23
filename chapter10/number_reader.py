from pathlib import Path
import json

path = Path("chapter10/numbers.json")
contents = path.read_text(encoding="utf-8")
numbers = json.loads(contents)
print(numbers)
