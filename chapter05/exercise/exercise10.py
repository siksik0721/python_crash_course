current_users = ["john", "jane", "mary", "tom", "harry"]

new_users = ["Jane", "Tom", "Brad", "Michael", "Emma"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("새 사용자 이름을 입력하세요.")
    else:
        print(f"해당 사용자 이름 {new_user}을 사용할 수 있습니다.")
