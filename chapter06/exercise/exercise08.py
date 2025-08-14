pet_0 = {"name": "뽀삐", "master": "철수"}
pet_1 = {"name": "멍멍이", "master": "영희"}

pets = []
pets.append(pet_0)
pets.append(pet_1)

for pet in pets:
    print(f"Name = {pet["name"]}, Master = {pet["master"]}")
