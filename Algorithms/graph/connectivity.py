a = []
n = 12
for i in range(n):
    tmp = []
    for j in range(n):
        tmpValue = 0
        if j == i:
            tmpValue = 1
        tmp.append(tmpValue)
    a.append(tmp)

file = open("connect.txt", "r")
for line in file:
    f = line.split(" ")
    i = int(f[0]) - 1
    j = int(f[1]) - 1
    a[i][j] = 1
    a[j][i] = 1


def warshall(a, n):
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if a[u][v] == 1 or (a[u][k] == 1 and a[k][v] == 1):
                    a[u][v] = 1


warshall(a, n)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')