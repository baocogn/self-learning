def read_input(n, m):
    rows = []
    for _ in range(n):
        row = list(map(int, input().split()))[:m]
        rows.append(row)
    return rows

def valid(i, j, n, m):
    if i >= n: return False
    if j >= m: return False
    if i < 0: return False
    if j < 0: return False
    return True

def positions(i, j, n, m):
    pos = []
    # On the same column
    for x in range(n): pos.append((x, j))
    # On the same row
    for y in range(m): pos.append((i, y))
    # Parallel to the main diagonal
    characteristic_1 = i - j
    for x in range(n): pos.append((x+characteristic_1, x))
    # Parallel to the secondary diagonal
    characteristic_2 = i + j
    for x in range(n): pos.append((x, characteristic_2-x))

    return pos

def process(n, m, rows):
    count = 0
    for i in range(n):
        for j in range(m):
            ps = positions(i, j, n, m)
            flag = True
            for p in ps:
                x, y = tuple(p)
                if valid(x, y, m, n):
                    if rows[x][y] > rows[i][j]:
                        flag = False
                        break
            if flag:
                count += 1
    return count

n = int(input())
rows = read_input(n, n)
print(process(n, n, rows))
