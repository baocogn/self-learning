def read_input():
    m, n = tuple(map(int, input().split()))

    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)

    return matrix, m, n

def process(matrix, m, n):
    results = []
    for col_j in range(n):
        flag = True
        for row_i in range(m):
            if matrix[row_i][col_j] > 0:
                flag = False
                break
        if flag:
            results.append(col_j)

    return results
        
matrix, m, n = read_input()
for col in process(matrix, m, n):
    print(col, end = " ")
