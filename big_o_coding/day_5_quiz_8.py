n = int(input())
ids = map(int, input().split())

def process(ids):
    ids = sorted(ids)
    for i in range(len(ids)-1):
        if ids[i+1] > ids[i] + 1:
            return ids[i] + 1
    return ids[len(ids)-1] + 1

print(process(ids))
