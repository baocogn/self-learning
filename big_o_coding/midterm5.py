def read_input():
    n = int(input())

    magnets = []
    for _ in range(n):
        magnet = input()
        magnets.append(magnet)

    return n, magnets

def process(n, magnets):
    count = 0
    prev = None
    for magnet in magnets:
        if prev != magnet:
            count += 1
        prev = magnet
    return count

n, magnets = read_input()
print(process(n, magnets))