from pathlib import Path
import json

path = Path("chapter10/exercise/favorite_num.json")

favorite_number = int(input("당신이 좋아하는 숫자는? "))
path.write_text(json.dumps(favorite_number))
