# complexity: O()
N = int(input())
a = list(map(int, input().split()))
Q = int(input())
q = list(map(int, input().split()))

x = 0
INF = int(1e9)
left = 0
right = N - 1
h1 = -1
h2 = INF

while left <= right:
    mid = left + (right - left)//2
    if a[mid] < x:
        h1 = max(h1, a[mid])
        left = mid + 1
    if a[mid] > x:
        h2 = min(h2, a[mid])
        right = mid - 1
    else:
        right = mid - 1
        left = mid + 1
 
if h1 == -1:
    print("X")
else:
    print(h1)
if h2 == INF:
    print("X")
else:
    print(h2)
