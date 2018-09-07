n = int(input())
l = list(map(int, input().split()))[:n]

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

is_even = []
odds = []
evens = []
for i in range(n):
    if l[i] % 2 == 0:
        is_even.append(True)
        evens.append(l[i])
    else:
        is_even.append(False)
        odds.append(l[i])

odds = merge_sort(odds)
evens = list(reversed(merge_sort(evens)))

results = []
odd, even = 0, 0
for i in range(n):
    if is_even[i]:
        results.append(evens[even])
        even += 1
    else:
        results.append(odds[odd])
        odd += 1

print(' '.join([str(x) for x in results]))
