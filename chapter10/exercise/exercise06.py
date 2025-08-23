first_number = input("First number: ")
second_number = input("Second number: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("숫자를 입력해야 합니다.")
else:
    print(first_number + second_number)
