a = int(input())

n = list(map(int, input().split()))

def insertion_sort(n):
    for i in range(1, len(n)):
        x = n[i]
        j = i
        while (j > 0) and (n[j-1] > x):
            n[j] = n[j-1]
            j -= 1
        n[j] = x
    return n

print(' '.join(str(x) for x in insertion_sort(n)))