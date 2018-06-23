#Two way Graph
a = []
n = 12
parent = []
noChildren = []
number = []
low = []
stack = []
top = [-1]
count = [-1]
isCut = []

for i in range(n):
    parent.append(-1)
    noChildren.append(0)
    number.append(-1)
    low.append(-1)
    isCut.append(False)


for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 1
        tmp.append(tmpValue)
    a.append(tmp)

file = open("directivity_bridges_cutverticles.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    a[i][j] = 1
    a[j][i] = 1

def visit(u, a, n, parent, number, low, count):
    count[0] = count[0] + 1
    number[u] = count[0]
    low[u] = n+10 #infinite value
    for v in range(n):
        if v == u:
            continue
        if a[u][v] == 1:
            a[v][u] = 0
            if parent[v] == -1:
                parent[v] = u
                visit(v, a, n, parent, number, low, count)
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], number[v])

for u in range(n):
    if parent[u] == -1:
        parent[u] = -10 #root
        visit(u, a, n, parent, number, low, count)

print(number)
print(low)
print(parent)
for v in range(n):
    u = parent[v]
    if low[v] >= number[v] and u != -10:
        print("bridge: {0} - {1} ".format(u, v))
for v in range(n):
    u = parent[v]
    if (u > -1):
        noChildren[u] = noChildren[u] + 1
print(noChildren)
for v in range(n):
    u = parent[v]
    if low[v] >= number[u] and u > -1:
        isCut[u] = isCut[u] or parent[u] > -1 or noChildren[u] >= 2
print(isCut)
