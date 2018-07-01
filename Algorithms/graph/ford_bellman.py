#Two way Graph
a = []
n = 6
nd = 7
d = []
trace=[]
start = 0
end = 3
maxC = 1000

for i in range(n):
    d.append(maxC)
    trace.append(-1)
    tmp = []
    for j in range(n):
        tmpValue = maxC
        if j == i:
            tmpValue = 0 #min path 0
        tmp.append(tmpValue)
    a.append(tmp)

d[start] = 0
file = open("minpath.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    k = int(f[2])
    a[i][j] = k
    a[j][i] = k

def ford_bellman(a, d, n, nd, start):
    for i in range(nd):
        stop = True
        for u in range(n):
            for v in range(n):
                if (d[v] > d[u] + a[u][v]):
                    d[v] = d[u] + a[u][v]
                    trace[v] = u
                    stop = False
        if stop:
            break

ford_bellman(a, d, n, nd, start)

print(d)
print(trace)

tracePoint = end
print(tracePoint, end = "<-")
while tracePoint != start:
    print(trace[tracePoint], end = "<-")
    tracePoint = trace[tracePoint]
