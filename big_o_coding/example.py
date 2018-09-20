def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:]) if i < len(left) else result.extend(right[j:])
    return result

def merge_sort(list):
    if len(list) < 2:
        return list
    mid = len(list) // 2
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


l = list(map(int, input().split()))

print(' '.join(str(x) for x in merge_sort(l)))