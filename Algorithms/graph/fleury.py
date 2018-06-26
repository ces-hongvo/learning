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

def canGoBack(x, y, a, n):
    queue = []
    free = []
    for i in range(n):
        free.append(True)
    a[x][y] = a[x][y] - 1
    a[y][x] = a[y][x] - 1
    free[y] = False
    front = 0
    rear = 0
    queue.append(y)
    while front <= rear:
        u = queue[front]
        front = front + 1
        for v in range(n):
            if free[v] and a[u][v] > 0:
                rear = rear + 1
                queue.append(v)
                free[v] = False
                if not free[x]:
                    break

    result = not free[x]
    a[x][y] = a[x][y] + 1
    a[y][x] = a[y][x] + 1
    return result

def findEulerCircuit(a, n):
    current = 0
    count = 1
    print(current)
    while True:
        next = -1
        for v in range(n):
            if a[current][v] > 0:
                next = v
                if canGoBack(current, v, a, n):
                    break
        if next != -1:
            a[current][next] = a[current][next] - 1
            a[next][current] = a[next][current] - 1
            print(next)
            current = next
        if next == -1:
            break

findEulerCircuit(a, n)