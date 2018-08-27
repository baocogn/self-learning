def read_input():
    m, n = tuple(list(map(int, input().split())))

    matrix = []
    for _ in range(m):
        rows = list(map(int, input().split()))[:n]
        matrix.append(rows)
    
    return matrix, m, n

def isMax(matrix, i, j):
    for x in range(len(matrix[i])):
        if matrix[i][j] < matrix[i][x]:
            return False
    return True
            
def isMin(matrix, i, j):
    for x in range(len(matrix)):
        if matrix[i][j] > matrix[x][j]:
            return False
    return True

def process(matrix, m, n):
    count = 0
    for j in range(n):
        for i in range(m):
            if isMin(matrix, i, j) and isMax(matrix, i, j):
                 count += 1
    return count

matrix, m, n = read_input()
print(process(matrix, m, n))