name = input()
count = 0
pointer = 'a'

for i in range(0, len(name)):
    distance = abs(ord(pointer) - ord(name[i]))
    if distance < 13:
        count += distance
    else:
        count += 26 - distance
    pointer = name[i]

print(count)