# if cnt != 2: -> invalid
# else: BGS(s, f)
from queue import Queue

MAX = 100
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]
dist = [-1 for i in range(MAX)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def BFS(s):
    visited[s] = False
    q = Queue()
    # q.push(s)
    # while len(q) != 0:
    #     u = q.pop()
    #     # for i in range(0, m):