users = ["admin", "john", "tom"]

for user in users:
    if user == "admin":
        print("관리자님 안녕하세요. 상태 보고서를 보시겠습니까?")
    else:
        print(f"{user.title()}님 안녕하세요, 다시 로그인해 주셔서 감사합니다.")
