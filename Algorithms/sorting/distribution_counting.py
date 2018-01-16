k = [1, 2, 2, 3, 0, 0, 1, 1, 3, 3]
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m = 4
n = 10
c = [0,0,0,0]
p = [0,0,0,0]
for i in range(n):
    c[k[i]] = c[k[i]] + 1
    p[k[i]] = c[k[i]]

for i in range(1,m):
    p[i] = p[i-1] + p[i]
print(p)

for i in range(n-1, -1, -1):
    v = k[i]
    x[p[v]-1] = k[i]
    p[v] = p[v] - 1
print(x)
