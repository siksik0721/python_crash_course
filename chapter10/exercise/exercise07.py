while True:
    print("종료하려면 'q'를 입력하세요.")
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("숫자를 입력해야 합니다.")
    else:
        print(first_number + second_number)
