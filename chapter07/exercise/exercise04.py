prompt = "\n어떤 토핑을 추가할까요?('quit'을 입력하면 종료합니다.) "

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"{topping}을 피자에 추가하겠습니다.")
