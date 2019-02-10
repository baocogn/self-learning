n = int(input())

l = [input() for i in range(n)]
polyhedrons = {'Tetrahedron':4, 'Cube':6, 'Octahedron':8, 'Dodecahedron':12, 'Icosahedron':20}
res = 0
for x in l:
    res += polyhedrons[x]
print(res)
