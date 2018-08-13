def read_input():
    m, n = tuple(list(map(int, input().split())))

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)
    
    return matrix, m, n

def countEven(matrix, m, n, row):
    count = 0
    for col in range(n):
        if matrix[row][col] % 2 == 0:
            count += 1
    return count

def process(matrix, m, n):
    max_occur = 0
    max_index = -1
    for i in range(m):
        final_count = countEven(matrix, m, n, i)
        if final_count > max_occur:
            max_occur = final_count
            max_index = i
    return max_index

matrix, m, n = read_input()
print(process(matrix, m, n))        