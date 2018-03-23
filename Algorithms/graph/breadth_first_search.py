# trace 1-5 (0-4)
a = []
trace = []
queue = []
n = 8
for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if (j == i):
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

def BFS(a, trace, u, n, queue):
    queue.append(u)
    front = 0
    while(front < len(queue)):
        currentV = queue[front]
        front += 1
        for i in range(n):
            if a[currentV][i] == 1 and trace[i] < 0:
                trace[i] = currentV
                queue.append(i)
    return

def fetchResult(a, s , f, trace):
    path = []
    i = f
    while i != s:
        path.insert(0, i)
        i = trace[i]
    path.insert(0, i)
    return path

BFS(a, trace, 0, n, queue)
print(trace)
print(fetchResult(a, 0, 4, trace))