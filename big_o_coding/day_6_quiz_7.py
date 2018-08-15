def read_input():
    m, n, x = tuple(list(map(int, input().split()))

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))[:n]
        matrix.append(row)
    return matrix, m, n

def countX(x):
    count = 0
    


