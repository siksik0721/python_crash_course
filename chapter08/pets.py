def describe_pet(animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")

print("########")

describe_pet("harry", "hamster")

print("########")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")

print("########")


def describe_pet_with_default(pet_name, animal_type="dog"):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_with_default(pet_name="willie")
describe_pet(pet_name="harry", animal_type="hamster")

# describe_pet()  # TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
