from pathlib import Path

path = Path("chapter10/pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)

print("########")

path = Path("chapter10/pi_digits.txt")
contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    print(line)
