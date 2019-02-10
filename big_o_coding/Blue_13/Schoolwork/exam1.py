# MUH and Important Things
def print_plan(plan):
    for task in plan:
        print(task[1], end = ' ')
    print()
 
n = int(input())
h = list(map(int, input().split()))
 
tasks = []
for i in range(n):
    tasks.append((h[i], i + 1))
tasks.sort()
swaps = []
for i in range(1, n):
    if len(swaps) >= 2:
        break
    if tasks[i - 1][0] == tasks[i][0]:
        swaps.append((i - 1, i))
if len(swaps) < 2:
    print('NO')
    exit()
print('YES')
print_plan(tasks)
tasks[swaps[0][0]], tasks[swaps[0][1]] = tasks[swaps[0][1]], tasks[swaps[0][0]] 
print_plan(tasks)
tasks[swaps[1][0]], tasks[swaps[1][1]] = tasks[swaps[1][1]], tasks[swaps[1][0]] 
print_plan(tasks)
