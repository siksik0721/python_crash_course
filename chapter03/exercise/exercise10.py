cities = ["new york", "london"]
print(cities)

cities.append("seoul")
print(cities)

cities.insert(1, "tokyo")
print(cities)

print(cities.pop())
print(cities)

del cities[0]
print(cities)

cities.remove("london")
print(cities)

cities = ["new york", "paris", "london", "tokyo", "madrid"]
print(cities)

print(sorted(cities))
print(cities)

print(sorted(cities, reverse=True))
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)
