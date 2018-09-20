n = int(input())
def maxDigit(n):
    ans = -1
    while(n > 0):
        x = n % 10
        if x > ans:
            ans = x
        n = n // 10
    return ans

print(maxDigit(n))