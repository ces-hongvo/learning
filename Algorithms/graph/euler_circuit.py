from __future__ import print_function
#Two way Graph
a = []
n = 4

for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 0 #assume no way to it self
        tmp.append(tmpValue)
    a.append(tmp)

file = open("fleury.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    k = int(f[2])
    a[i][j] = k
    a[j][i] = k

def findEulerCircuit(a, n):
    stack = [0]
    top = 0
    count = 0
    while top > -1:
        u = stack[top]
        for v in range(n):
            if a[u][v] > 0:
                a[u][v] = a[u][v] - 1
                a[v][u] = a[v][u] - 1
                stack.append(v)
                top = top + 1
                break
        if u == stack[top]:
            print(stack.pop(), end=" ")
            top = top - 1

findEulerCircuit(a, n)