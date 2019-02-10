def binarySearch(a, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2 # if mid = (right + left) // 2 overfloat
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
if __name__ == '__main__':
    n, x = map(int, input().split()) # n: len(a), x: value
    a = list(map(int, input().split()))
    result = binarySearch(a, 0, n-1, x)
    print(result) # result is index
