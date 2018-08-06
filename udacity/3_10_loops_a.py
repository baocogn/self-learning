cities = ["new york", "chicago", "los angeles", "tokyo", "seoul"]

for city in cities:
    city = city.title()
    print(city)

# use the append method to add items into the list
for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)
