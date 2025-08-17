def make_album(musician, album, count=None):
    album = {"musician": musician, "album": album}
    if count:
        album["count"] = count
    return album


print(make_album("marvin gaye", "what's going on"))
print(make_album("beach boys", "pet sounds"))
print(make_album("beatles", "abbey road", 17))
