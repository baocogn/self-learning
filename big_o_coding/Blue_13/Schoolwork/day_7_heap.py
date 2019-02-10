# NORMAL HEAP (MIN) 
def MinHeapify(i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(a) and a[left] < a[smallest]:
        smallest = left
    if right < len(a) and a[right] < a[smallest]:
        smallest = right
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
    
def BuildHeap(n):
    for i in range(n//2 -1, -1, -1):
        MinHeapify(i)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    BuildHeap(len(a))
    print(a)
