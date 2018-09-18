def read_input():
    m, n, x = list(map(int, input().split()))

    matrix = []
    for _ in range(m):
        rows = list(map(int, input().split()))[:n]
        matrix.append(rows)
    return matrix, m, n, x

def countX(matrix, x, m, n):
    count = 0
    for col_j in range(n):
        for row_i in range(m):
            if matrix[row_i][col_j] == x:
                count += 1
    return count

matrix, m, n, x = read_input()
print(countX(matrix, x, m, n))