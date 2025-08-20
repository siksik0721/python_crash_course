from random import choice

lotto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]
hits = []
for i in range(4):
    hits.append(choice(lotto))

my_ticket = []
num = 0
while True:
    num += 1

    for i in range(4):
        my_ticket.append(choice(lotto))

    if my_ticket == hits:
        print(f"{num}번 시도하여 당첨되었습니다.")
        break
    else:
        my_ticket = []
