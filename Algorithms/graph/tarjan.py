#One way Graph
a = []
n = 11
free = []
number = []
low = []
stack = []
top = [-1]
count = [-1]

for i in range(n):
    free.append(True)
    number.append(-1)
    low.append(-1)

for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 1
        tmp.append(tmpValue)
    a.append(tmp)

file = open("tarjanMap.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    a[i][j] = 1


def visit(u, a, n, free, number, low, stack, top, count):
    count[0] = count[0] + 1
    number[u] = count[0]
    low[u] = number[u]
    stack.append(u)
    top[0] = top[0] + 1
    for v in range(n):
        if (free[v] and a[u][v] > 0):
            if(number[v] > -1):
                low[u] = min(low[u], number[v])
            else:
                visit(v, a, n, free, number, low, stack, top, count)
                low[u] = min(low[u], low[v])
    if low[u] == number[u]:
        v = -1
        while(v != u):
            v = stack.pop()
            free[v] = False
        print(u)
    return

for u in range(n):
    if (number[u] == -1):
        visit(u, a, n, free, number, low, stack, top, count)

print(low)
print(number)