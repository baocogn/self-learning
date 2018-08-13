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
    for i in range(2, int(x ** 0.5 +1)):
        if x % i == 0:
            return False
    return True

def process(matrix, m):
    results = 1
    for row_i in range(m):
        if isPrime(matrix[row_i][m - 1 - row_i]):
                results = (results * matrix[row_i][m - 1 - row_i]) % 1000003
    return results
matrix, m = read_input()
print(process(matrix, m))