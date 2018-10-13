n, a, b = map(int, input().split())
l = list(map(int, input().split()))[:n]

j = 0
count = 0

def insertion_sort(l):
    for i in range(1, len(l)):
        x = l[i]
        j = i
        while (j > 0) and (l[j-1] < x):
            l[j] = l[j-1]
            j -= 1
        l[j] = x
    return l

h = insertion_sort(l)

x = h[a-1] - h[a]

print(x)