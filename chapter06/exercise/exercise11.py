cities = {}
cities["seoul"] = {"country": "korea", "population": 9323492, "fact": "asia"}
cities["tokyo"] = {"country": "japan", "population": 14042127, "fact": "asia"}
cities["london"] = {"country": "england", "population": 8825001, "fact": "europe"}

for name, city in cities.items():
    print(f"{name}")
    for info_name, city_info in city.items():
        print(f"\t{info_name} = {city_info}")
