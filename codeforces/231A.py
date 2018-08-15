def read_input():
    n = int(input())
    rows =[]
    for _ in range(n):
        row = list(map(int, input().split()))
        rows.append(row)
    return rows, n

def process(rows, n):
    result = 0
    for row in rows:
        count_1, count_0 = 0, 0
        for x in row:
            if x == 1:
                count_1 += 1
            if x == 0:
                count_0 += 1
        if count_1 > count_0:
            result += 1
    
    return result

rows, n = read_input()
print(process(rows, n))   