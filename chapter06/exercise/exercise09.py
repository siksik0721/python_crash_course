favorite_places = {}
favorite_places["철수"] = ["서울", "도쿄"]
favorite_places["영희"] = ["파리", "로마"]

for name, places in favorite_places.items():
    print(f"{name}가 좋아하는 장소:")
    for place in places:
        print(f"\t{place}")
