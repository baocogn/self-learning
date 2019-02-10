import queue
Q = int(input())
 
for _ in range(Q):
	q = queue.Queue()
	pq = queue.PriorityQueue()
 
	n, m = map(int, input().split())
	prior = list(map(int, input().split()))
 
	for i in range(n):
		q.put((i, prior[i]))
		pq.put(-prior[i])
 
	count = 0
 
	while not pq.empty():
		jobPos, jobPrior = q.get()
		prior = -pq.get()
 
		if prior == jobPrior:
			count += 1
			if jobPos == m:
				break
		else:
			q.put((jobPos, jobPrior))
			pq.put(prior)
 
	print(count)
    