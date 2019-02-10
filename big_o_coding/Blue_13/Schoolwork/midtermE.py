n = int(input())
numbers = list(map(int, input().split()))

b = sorted(numbers, reverse = False)

for i in range(n):
    if i == round(n//2):
        print(b[i])