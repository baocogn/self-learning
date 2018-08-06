# s = input()

# def palindrome(s):
#     n = len(s)
#     for i in range(int(n / 2)):
#         if s[i] != s[n-1-i]:
#             return False
#     return True

# if palindrome(s):
#     print("YES")
# else:
#     print("NO")

n = int(input())

def reverse(n):
    count = 0
    while n != 0:
        a = n % 10
        n = n // 10
        count = count * 10 + a
    return count

if reverse(n) == n:
    print("YES")
else:
    print("NO")
