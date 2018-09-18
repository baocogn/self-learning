n, k = map(int, input().split())

scores = list(map(int, input().split()))

def process(scores, n, k):
    count = 0
    for i in range(n):
        if scores[i] <= 0:
            break
        if i >= k and scores[i-1] > scores[i]:
            break
        count = count + 1        
    return count

print(process(scores, n, k))
