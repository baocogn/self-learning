import sys
sys.setrecursionlimit(10000)

n = int(input())

a = list(map(int, input().split()))

def sumEven(a, x):
    if x == -1:
        return 0
    if a[x] % 2 == 0:
        return a[x] + sumEven(a, x-1)
    else:
        return sumEven(a, x-1)

print(sumEven(a, n-1))     