x = int(input())

first_steps = x // 5
remainder = x % 5

if remainder == 0:
    print(first_steps)
else:
    print(first_steps + 1)