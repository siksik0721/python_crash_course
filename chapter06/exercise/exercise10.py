favorite_numbers = {
    "철수": [1],
    "영희": [5, 9],
    "영수": [8, 10],
    "영철": [3, 4],
    "정숙": [12],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}이/가 좋아하는 숫자:")
    for number in numbers:
        print(f"\t{number}")
