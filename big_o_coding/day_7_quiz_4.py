n = int(input())
for _ in range(n):
    name = str(input())
    res = ""
    for i in range(len(name)):
        if i == 0 or name[i-1] == ' ':
            if 'a' <= name[i] <= 'z':
                ch = name[i].upper()
                res += ch
            else:
                res += name[i]
        else:
            if 'A' <= name[i] <= 'Z':
                ch = name[i].lower()           
                res += ch
            else:
                res += name[i]
    print(res)
      