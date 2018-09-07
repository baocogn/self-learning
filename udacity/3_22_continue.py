fruits = ["orange", "apple", "durian", "watermelon"]
foods = ["apple", "apple", "hummus", "toast"]

fruit_count = 0
for food in foods:
    if food not in fruits:
        print("NOT A FRUIT")
        continue
    fruit_count += 1
    print("FOUND A FRUIT")

print("TOTAl FRUIT: ", fruit_count)