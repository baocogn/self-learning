n = int(input())

a = list(map(int, input().split()))


def Insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i
        while (j > 0) and (a[j-1] < x):
            a[j] = a[j-1]
            j -= 1
        a[j] = x
    return a

print(' '.join(str(x) for x in Insertion_sort(a)))