# Time limit!

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# sorted(a, reverse = False)
# res = 0
# for i in range(0, n):
#     if a[i] + k in a:
#         res += 1
# print(res)

def binarySearch(a, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2 # if mid = (right + left) // 2 overfloat 
        if x == a[mid]:
            return mid   
        elif x < a[mid]:
            right = mid - 1    
        else:
            left = mid + 1
    
    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a = sorted(a, reverse = False)
    cnt = 0
    for i in range(len(a)):
        if binarySearch(a, 0, n-1, k+a[i]) != -1:
            cnt += 1
    
    print(cnt)
