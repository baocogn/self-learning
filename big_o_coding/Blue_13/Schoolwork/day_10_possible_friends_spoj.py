#                         SOCIALNE - Possible Friends

# Josué, one of the undergraduate students in PUCMM, is developing a 
# Social Network, but he is having difficulties in identifying the person 
# that has more possible friends. 
# Two persons are possible friends if they are not friends and they have 
# at least one common friend, for example if person A is friend only to 
# person B, and person B is friend of C, then, A and C are possible 
# friends. 
# You are about to help him in this task. Given the network table, you 
# have to write a program that finds the person that has more possible 
# friends, if more than one person matches this criteria, then select 
# the one that comes first ( the one that has the lower ID).

# Input
# The first line is T (1 ≤ T ≤ 1,000), the number of test cases, then T 
# test cases follow.

# Each test case consists in a 'Y' or 'N' square matrix(MxM) representing 
# the friendship of the network, where M is the number of persons.

# Constraints
# M (1 ≤ M ≤ 50)

# The square matrix has M lines, each line has M characters.
# The first line of the matrix corresponds to person 0, the next line to
# person 1, and so on.
# On each line the leftmost character corresponds to person 0, the next 
# character to person 1, and so on.
# So if character j of the line i is 'Y', it means that person 'i' is a 
# friend of 'j'.
# For each person i, character i of line i will be 'N'.
# For each i,j character j of line i will be the same as character i of 
# line j.

# Output
# For each test case, you have to output one line containing the ID of 
# the person(0-based) that has more possible friends and the number of 
# possible friends this person has, separated by a blank space.
import queue
MAX = 100
INF = int(1e9)

def printPath(s, t):
    b = []
    while s != t:
        b.append(t)
        t = path[s][t]
    b.append(s)
    for i in range(len(b)-1, -1, -1):
        print(b[i], end=' ' if i > 0 else '\n')

def FloydWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

if __name__ == '__main__':
    n = int(input())
    graph = [[None for i in range(n)] for j in range(n)]
    dist = [[None for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        line = list(input())
        for j in range(n):
            if graph[i][j] == "Y":
                graph[i][j] = 1
            elif i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = INF
    
    for i in range(0, n-1):
        cnt = 0
        maxfriend = 0
        minid = -1
        for j in range(0, -1):
            if dist[i][j] == 2:
                cnt += 1
        if cnt > maxfriend:
            maxfriend = cnt
            minid = i

    FloydWarshall(graph, dist)
    printPath(minid, maxfriend)
    print(dist[minid][maxfriend])
