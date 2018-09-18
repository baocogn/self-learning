# def process(counts):
#     min_char = None
#     min_count = None
#     for char in counts:
#         if (min_count is None) or \
#            (counts[char] < min_count) or \
#            (counts[char] == min_count and ord(char) < ord(min_char)):
#             min_count = counts[char]
#             min_char = char

#     return min_char

# for _ in range(n):
#     counts = dict()
#     string = input()
#     for char in string:
#         char = char.upper()
#         counts.setdefault(char, 0)
#         counts[char] += 1
#     print(process(counts))

def getPos(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    return ord(char) - ord('a')

def getminChar(string):
    count = [0] * 26
    for char in string:
        count[getPos(char)] += 1
    min_ch = 1001
    res = ""
    for i in range(len(count)):
        if count[i] < min_ch:
            min_ch = count[i]
            res = chr(i + ord('A'))
    return res

n = int(input())

for _ in range(n):
    s = input()
    print(getminChar(s))