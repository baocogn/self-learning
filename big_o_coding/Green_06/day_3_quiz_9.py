n = int(input())

sum, sum_i, i = 0, 0, 1

while True:
    sum_i += i
    sum += sum_i
    if sum > n:
        print(i-1)
        break
    i += 1
