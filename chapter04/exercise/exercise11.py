pizzas = ["페퍼로니", "치즈", "하와이안"]
friend_pizzas = pizzas[:]

pizzas.append("슈프림")
friend_pizzas.append("불고기")

print("내가 좋아하는 피자는:")
for pizza in pizzas:
    print(pizza)

print("내 친구가 가장 좋아하는 피자는:")
for pizza in friend_pizzas:
    print(pizza)
