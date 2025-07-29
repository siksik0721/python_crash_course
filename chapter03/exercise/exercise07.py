guests = ["철수", "영희", "영수"]
print(f"{guests[0]}야, 저녁 식사에 와.")
print(f"{guests[1]}야, 저녁 식사에 와.")
print(f"{guests[2]}야, 저녁 식사에 와.")

print("더 큰 테이블을 찾았습니다.")

guests.insert(0, "영호")
guests.insert(2, "순자")
guests.append("상철")
print(f"{guests[0]}야, 저녁 식사에 와.")
print(f"{guests[1]}야, 저녁 식사에 와.")
print(f"{guests[2]}야, 저녁 식사에 와.")
print(f"{guests[3]}야, 저녁 식사에 와.")
print(f"{guests[4]}야, 저녁 식사에 와.")
print(f"{guests[5]}야, 저녁 식사에 와.")

print("저녁 식사에 두 명만 초대할 수 있게 되었습니다.")

print(f"{guests.pop()}야, 미안해.")
print(f"{guests.pop()}야, 미안해.")
print(f"{guests.pop()}야, 미안해.")
print(f"{guests.pop()}야, 미안해.")

print(f"{guests[0]}야, 저녁 식사는 취소되지 않았어.")
print(f"{guests[1]}야, 저녁 식사는 취소되지 않았어.")

del guests[0]
del guests[0]
print(guests)
