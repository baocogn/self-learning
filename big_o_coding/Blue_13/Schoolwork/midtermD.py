dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
 
def BFS(sr, sc, fr, fc):
	left = right = 0
	q[0] = (sr, sc)
	graph[sr][sc] = 1
 
	while left <= right:
		ur, uc = q[left]
		left += 1
 
		if ur == fr and uc == fc:
			break
 
		for i in range(4):
			r = ur + dr[i]
			c = uc + dc[i]
 
			if r in range(R) and c in range(C) and graph[r][c] == 0:
				graph[r][c] = graph[ur][uc] + 1
				right += 1
				q[right] = (r, c)
 
	return graph[fr][fc] - 1
 
while True:
	R, C = map(int, input().split())
 
	if R == 0 and C == 0:
		break
 
	graph = [[0] * C for _ in range(R)]
	q = [None] * R * C
 
	rows = int(input())
 
	for _ in range(rows):
		cols = list(map(int, input().split()))
		row = cols.pop(0)
		n = cols.pop(0)
 
		for col in cols:
			graph[row][col] = -1
 
	sr, sc = map(int, input().split())
	fr, fc = map(int, input().split())
 
	print(BFS(sr, sc, fr, fc))
    