from pathlib import Path

path = Path("chapter10/pi_digits.txt")
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

print("########")

path = Path("chapter10/pi_million_digits.txt")
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
