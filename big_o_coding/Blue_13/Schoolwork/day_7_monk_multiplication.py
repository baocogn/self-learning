import sys
sys.setrecursionlimit(10**5)

n = int(input())
a = list(map(int, input().split()))

import heapq
heapq._heapify_max(a)

# class PQEntry:
#     def __init__(self, value):
#         self.value = value
#     def __lt__(self, other):
#         return self.value > other.value

# h = []
# for x in a:
#     heapq.heappush(h, PQEntry(x))

res = []

for i in range(len(a)):
    if i < 2:
        res.append(-1)
    else:
        if a

