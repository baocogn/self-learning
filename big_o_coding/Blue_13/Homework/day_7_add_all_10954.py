n = int(input())
h = list(map(int, input().split()))

def MinHeapify(i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
    
def BuildHeap(n):
    for i in range(n//2 -1, -1, -1):
        MinHeapify(i)

BuildHeap(n)

for _ in range(0, n-1):
    first = h.pop(0)
    second = h.pop(0)
    res = (first + second)
    h.append(first+second)
print(res)
