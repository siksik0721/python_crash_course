sandwich_orders = ["에그마요", "터키", "스테이크앤치즈"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich} 샌드위치를 만들었습니다.")
    finished_sandwiches.append(sandwich)

print("\n현재까지 만든 샌드위치는 다음과 같습니다:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich}")
