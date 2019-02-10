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
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split()) # n: len(a), m: price of the pizza
        a = list(map(int, input().split()))
    
        count = 0
        a = sorted(a, reverse = False)

        for i in range(len(a)):
            result = binarySearch(a, 0, n-1, m-a[i])
            if result != -1 and result > i: 
                count += 1
                
        print(count)