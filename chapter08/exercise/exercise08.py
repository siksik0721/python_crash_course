def make_album(musician, album, count=None):
    album = {"musician": musician, "album": album}
    if count:
        album["count"] = count
    return album


while True:
    musician = input("음악가를 입력하세요: ")
    album = input("앨범 타이틀을 입력하세요: ")

    print(make_album(musician, album))

    repeat = input("그만하시겠습니까? (yes / no) ")
    if repeat == "yes":
        break
