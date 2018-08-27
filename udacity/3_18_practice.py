number = int(input())
product = number

# first way:
for num in range(1, number):
    product *= num

print(product)

# second way:
while number > 1:
    number -= number
    product *= number

print(product)