n, x = map(int, input().split())
lessons = list(map(int, input().split()))
lessons.sort()

ans = 0
for chapter in lessons:
	ans += chapter * x
	if x > 1:
		x -= 1

print(ans)
