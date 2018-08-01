n, m, a = map(int, input().split())

r = n % a
height = n // a
if r != 0:
    height = height + 1

r = m % a
width = m // a
if r != 0:
    width = width + 1

print(height, width)