# n = int(input())
# s = input()

# # if len(s) < 26:
# #     print("NO")

# def isPangram(phrase):
#     lowercase = "abcdefghijklmnopqrstuvwxyz"
#     uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter = " "
#     count = 0
#     for i in range(len(lowercase)):
#         for char in phrase:
#             if lowercase[i] == char: 
#                 letter += char
#                 count += 1
#     for j in range(len(uppercase)):
#         for char in phrase:
#             if uppercase[j] == char:            
#                 letter += char
#                 count += 1
#     if count >= 26:
#         return True

# if isPangram(s):
#     print("YES")
# else:
#     print("NO")   

n = int(input())
s = input()
if len(set(s.lower()))<26:
    print("NO")
elif len(set(s.upper()))<26:
    print("NO")
else:
    print("YES")
# elif len(set(input().upper()))<26]):
#     print("NO")
