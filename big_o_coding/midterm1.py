n = int(input())

result = 1

if n == 1:
    result = 1 * 15000
elif 2 <= n <= 5:
    result = 1 * 15000 + (n - 1) * 13500
elif 6 <= n <= 11:
    result = 1 * 15000 + 4 * 13500 + (n - 5) * 11000
elif n >= 12:
    result = int((1 * 15000 + 4 * 13500 + (n - 5) * 11000) * (1 - 0.1))

print(result )