n, x = map(int(input().split()))
numbers = list(map(int, input().split()))

count = 0
def index(a):
    for i in range (len(numbers)):
        if numbers[i] != x:
            count += 1
        else:
            return count
    return count

print()       