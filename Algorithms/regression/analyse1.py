n = 5
x = []

for i in range(n+1):
    tmp = []
    for j in range(n+1):
        tmp.append(0)
    x.append(tmp)

x[0][0] = 1

for r in range(1, n+1):
    for c in range(0, n+1):
        if r > c:
            x[r][c] = x[r-1][c]
        else:
            x[r][c] = x[r-1][c] + x[r][c-r]

print(x)
