start_num = 10
end_num = 100
count_by = 3

# 1
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# 2
if end_num < start_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    
    result = break_num

print(result)

# 3
limit = 40

# write your while loop here
a = 0
while (a+1)**2 < limit:
    a += 1
nearest_square = a**2

print(nearest_square)