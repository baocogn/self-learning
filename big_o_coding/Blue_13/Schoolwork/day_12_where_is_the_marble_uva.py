def binarySearch(a, left, right, x):
    while left < right:
        mid = left + (right - left) // 2
        if x == a[mid]:
            return mid 
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    while True:
        n, q = map(int, input().split())
        if n == q == 0:
            break
        l = []
        for _ in range(n):
            a = int(input())
            l.append(a)
        ll = sorted(l, reverse = False)

        for _ in range(q):
            qs = int(input())
            res = binarySearch(ll, 0, n-1, qs) + 1
            if res == 0:
                print("{} not found".format(qs))
            else:
                print("{} found at {}".format(qs, res))
   