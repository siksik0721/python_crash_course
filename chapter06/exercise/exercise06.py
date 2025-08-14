favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

participants = ["jen", "charles", "edward", "john"]
for name in participants:
    if name in favorite_languages.keys():
        print(f"{name}, thank you for taking the poll!")
    else:
        print(f"{name}, please take our poll.")
