# 1

# cities = ['new york city', 'chicago', 'los angeles', 'beijing', 'sai gon']

# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())
#     # capitalized_cities.append(city.upper())

# print(capitalized_cities)

# or:
# capitalized_cities = [city.title() for city in cities]

# 2

# squares = []
# for x in range(9):
#     squares.append(x**2)
#     # print(squares)
# print(squares)

square = [x**2 if x % 2 == 0 else x + 3
for x in range(9)]
print(square)

square = [x**2 for x in range(9) if x % 2 == 0]
print(square)