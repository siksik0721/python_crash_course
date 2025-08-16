places = []
while True:
    place = input("\nIt you could visit one place in the world, where would you go? ")
    places.append(place)

    quit = input("Quit? (yes / no) ")
    if quit == "yes":
        break

print("\n--- Result ---")
for place in places:
    print(f"\t{place}")
