from __future__ import print_function
#Two way Graph
a = []
n = 6
d = []
free=[]
trace=[]
pos=[]
heap=[]
nHeap = [0]
start = 0
end = 3
maxC = 1000 #max distance


for i in range(n):
    d.append(maxC)
    free.append(True)
    trace.append(-1)
    pos.append(-1)
    heap.append(1000)
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

def update(v, nHeap, heap, d, pos):
    child = pos[v]
    if child < 0:
        nHeap[0] += 1
        child = nHeap[0] - 1
    parent = (child - 1) // 2
    while parent >= 0 and (d[heap[parent]] > d[v]):
        heap[child] = heap[parent]
        pos[heap[child]] = child
        child = parent
        parent = (child - 1) // 2
    heap[child] = v
    pos[v] = child

def pop(nHeap, heap, d, pos):
    popValue = heap[0]
    v = heap[nHeap[0] - 1]
    nHeap[0] -= 1
    r = 0
    while (r * 2) + 1 < nHeap[0]:
        c = (r * 2) + 1
        if c < nHeap[0] and d[heap[c]] > d[heap[c+1]]:
            c = c + 1
        if d[heap[c]] > d[v]:
            break
        heap[r] = heap[c]
        pos[heap[r]] = r
        r = c
    heap[r] = v
    pos[v] = r
    if nHeap[0] < len(heap):
        heap[nHeap[0]] = 1000
    return popValue

def dijkstra(a, s, f, nHeap, heap, d, pos, free, trace):
    update(s, nHeap, heap, d, pos)
    while True:
        u = pop(nHeap, heap, d, pos)
        if u == f:
            break
        free[u] = False
        for iv in range(len(a)):
            v = iv
            if free[v] and d[v] > d[u] + a[u][v]:
                d[v] = d[u] + a[u][v]
                trace[v] = u
                update(v, nHeap, heap, d, pos)
        if nHeap[0] <= 0:
            break

dijkstra(a, start, end, nHeap, heap, d, pos, free, trace)

print(d)
print(trace)

tracePoint = end
print(tracePoint, end="<-")
while tracePoint != start:
    print(trace[tracePoint], end="<-")
    tracePoint = trace[tracePoint]
