def sumPower(x):
    sum = 0
    for i in range(1, x + 1):
        sum = sum + i**i
    return sum

n = int(input())
print(sumPower(n))

        