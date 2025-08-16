current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("########")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

print("########")

x = 1
while x <= 5:
    print(x)
    x += 1  # 생략하면 이 루프는 영원히 실행됩니다
