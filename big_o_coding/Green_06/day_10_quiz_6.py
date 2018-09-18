class Color:
    def __init__(self, code, length, count):
        self.code = code
        self.count = count
        self.length = length

n = int(input())
colors = {}
for _ in range(n):
    code, length = map(int, input().split())
    colors.setdefault(code, Color(code, 0, 0))
    colors[code].count += 1
    colors[code].length += length

print(len(colors))
for code in sorted(colors):
    color = colors[code]
    print("%d %d %d" % (color.code, color.length, color.count))
