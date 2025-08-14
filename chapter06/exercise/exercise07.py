people_0 = {"first_name": "철수", "last_name": "김", "age": 20, "city": "Seoul"}
people_1 = {"first_name": "영희", "last_name": "이", "age": 30, "city": "Busan"}
people_2 = {"first_name": "영수", "last_name": "박", "age": 40, "city": "Incheon"}

people = []
people.append(people_0)
people.append(people_1)
people.append(people_2)

for p in people:
    print(
        f"First name = {p["first_name"]}, Last name = {p["last_name"]}, Age = {p["age"]}, City = {p["city"]}"
    )
