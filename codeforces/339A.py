seq = input().split("+")
seq.sort()
res = seq[0]

for i in range(len(seq)-1):
    res = res + "+" + seq[i+1]
print(res)