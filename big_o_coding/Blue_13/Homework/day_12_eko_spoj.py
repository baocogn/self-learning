import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
heights = list(map(int, input().split()))
 
def getCutted(height):
  return sum(max(0, h - height) for h in heights)
 
left = 0
right = max(heights)
res = 0
 
while (left <= right):
  mid = left + (right - left) // 2
  if getCutted(mid) >= M:
    res = mid
    left = mid + 1
  else:
    right = mid - 1
 
print(res)