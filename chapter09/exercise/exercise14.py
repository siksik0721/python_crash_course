from random import choice

lotto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]
for i in range(4):
    print(choice(lotto))
print("이와 일치하는 티켓에 상금을 지급합니다")
