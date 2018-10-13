n = int(input())
names = []
for _ in range(n):
    names.append(input())

def merge(Left, Right):
    l, r = 0, 0
    results = []
    while l < len(Left) and r < len(Right):
        if Left[l] > Right[r]:
            results.append(Left[l])
            l += 1
        elif Left[l] <= Right[r]:
            results.append(Right[r])
            r += 1
    results.extend(Right[r:]) if r < len(Right) else results.extend(Left[l:])
    return results

def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))

print('\n'.join([x for x in reversed(merge_sort(names))]))
