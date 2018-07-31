#Two way Graph
a = []
n = 6
d = []
free=[]
trace=[]
start = 0
end = 3
maxC = 1000 #max distance

for i in range(n):
    d.append(maxC)
    free.append(True)
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

def dijkstra(a, n, d, free, start, end, trace):
    while True:
        u = 0;
        min = 1000;
        for i in range(n):
            if free[i] and d[i] < min:
                min = d[i]
                u = i
        if u == -1 or u == end:
            break
        free[u] = False
        for v in range(n):
            if free[v] and d[v] > d[u] + a[u][v]:
                d[v] = d[u] + a[u][v]
                trace[v] = u

dijkstra(a, n, d, free, start, end, trace)

print(d)
print(trace)

tracePoint = end
print(tracePoint, end = "<-")
while tracePoint != start:
    print(trace[tracePoint], end = "<-")
    tracePoint = trace[tracePoint]