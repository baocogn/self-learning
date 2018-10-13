n, m, x, y = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = [0, 0]
j = 0
# for i in range(1, n):
#     while j < m:
#         if b[j] in (a[i] - x, a[i] + y):
#             res = [a[i], b[j]]
#         elif b[j] > a[i] + y:
