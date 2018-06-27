#Two way Graph
a = []
x = []
n = 5
free = []

for i in range(n):
    free.append(True)
    x.append(-1)
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 0 #assume no way to it self
        tmp.append(tmpValue)
    a.append(tmp)

file = open("hamilton.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    a[i][j] = 1
    a[j][i] = 1
print(a)
def tryFind(i, a, x, n, free):
    for j in range(n):
        if free[j] and a[x[i-1]][j] > 0:
            x[i] = j
            if i < n-1:
                free[j] = False
                h = i + 1
                tryFind(h, a, x, n, free)
                free[j] = True
            else:
                if a[j][x[0]] > 0:
                    x.append(x[0])
                    print(x)
                    x.pop()

x[0] = 0
free[0] = False
tryFind(1, a, x, n, free)