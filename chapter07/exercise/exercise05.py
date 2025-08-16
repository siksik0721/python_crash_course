prompt = "\n나이를 입력하세요(종료하려면 'quit'을 입력하세요): "

while True:
    age = input(prompt)
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("무료입니다.")
        elif age < 12:
            print("10달러입니다.")
        else:
            print("15달러입니다.")
