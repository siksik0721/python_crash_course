sandwich_orders = ["에그마요", "훈제 터키", "터키", "훈제 햄", "스테이크앤치즈"]
finished_sandwiches = []

print("훈제 메뉴는 품절입니다.")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if "훈제" not in sandwich:
        print(f"{sandwich} 샌드위치를 만들었습니다.")
        finished_sandwiches.append(sandwich)

print("\n현재까지 만든 샌드위치는 다음과 같습니다:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich}")
