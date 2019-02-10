n = int(input())
max = 0
passengers = 0

for i in range(n):
    a, b = map(int,input().split(" "))
    passengers -= a
    passengers += b
    if max < passengers: 
        max = passengers

print(max)
