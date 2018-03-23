# trace 1-5 (0-4)
a = []
trace = []
n = 8
for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 1
        tmp.append(tmpValue)
    a.append(tmp)
    trace.append(-1)

file = open("map00.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    a[i][j] = 1
    a[j][i] = 1


def DFS(a, trace, u, n):
    for i in range(n):
        if a[u][i] == 1 and trace[i] < 0:
            trace[i] = u
            DFS(a, trace, i, n)
    return

def fetchResult(a, s , f, trace):
    path = []
    i = f
    while i != s:
        path.insert(0, i)
        i = trace[i]
    path.insert(0, i)
    return path


DFS(a, trace, 0, n)
print(trace)
print(fetchResult(a, 0, 4, trace))
