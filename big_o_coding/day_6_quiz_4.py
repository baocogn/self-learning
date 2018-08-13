def read_input(): 
    m = int(input())
    
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix, m

def isPrime(x):
    if x <= 1:
        return False
    for k in range(2, int(x ** 0.5 + 1)):
        if x % k == 0:
            return False
    return True

def isDiagonal(i, j):
    if i == j:
        return True
    return False

def process(matrix):
    results = 0
    for col_j in range(m):
        for row_i in range(m):
            if isDiagonal(row_i, col_j) and isPrime(matrix[row_i][col_j]):
                results += 1
    return results

matrix, m = read_input()
print(process(matrix))
