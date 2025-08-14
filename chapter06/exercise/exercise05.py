rivers = {"나일강": "이집트", "한강": "대한민국", "아마존강": "브라질"}

for name, country in rivers.items():
    print(f"{name}은 {country}을/를 가로지릅니다.")
for name in rivers.keys():
    print(name)
for country in rivers.values():
    print(country)
