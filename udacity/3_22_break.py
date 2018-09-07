fruits = [("apples", 15), ("oranges", 30), ("grapes", 25), ("durians", 10)]

weight = 0
items = []

for cargo in fruits:
    print("current weight: {}".format(weight))
    if weight >= 100:
        (print("breaking loop now!"))
        break
    else:
        print("adding {} ({})".format(cargo[0], cargo[1]))
        items.append(cargo[0])
        weight += cargo[1]

print(weight)
print(items)
print(cargo[1])

