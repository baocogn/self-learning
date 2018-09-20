def read_input():
    m, n = tuple(list(map(int, input().split())))
    
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)

    return matrix, m, n

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

# assert(isPrime(1) == False)
# assert(isPrime(2) == True)
# assert(isPrime(4) == False)
# assert(isPrime(101) == True)

def isEdge(i, j, m, n):
    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
        return True
    return False

# assert(isEdge(0, 0, 100, 100) == True)

def process(matrix, m, n):
    results = 0
    for col_j in range(n):
        for row_i in range(m):
            if isEdge(row_i, col_j, m, n):
                if isPrime(matrix[row_i][col_j]):
                    results += 1
    return results

matrix, m, n = read_input()
print(process(matrix, m, n))
