n = 5
m = 11
w = [0, 3, 4, 5, 9, 4]
v = [0, 3, 4, 4, 10, 4]
f = []
for i in range(n+1):
    tmp = []
    for j in range(m+1):
        tmp.append(0)
    f.append(tmp)

def optimize(n, m, w, v, f):
    for i in range(1,n+1):
        for j in range(m+1):
            f[i][j] = f[i-1][j]
            if(j >= w[i] and f[i][j] < f[i-1][j-w[i]] + v[i]):
                f[i][j] = f[i - 1][j - w[i]] + v[i]

def trace(n, m, w, v, f):
    result = []
    j = m
    for i in range(n, -1, -1):
        if f[i][j] != f[i-1][j]:
            result.insert(0, i)
            j = j - w[i]
    return result

optimize(n, m, w, v, f)
for i in range(n+1):
    for j in range(m+1):
        print(f[i][j], end="\t")
    print("")
result = trace(n, m, w, v, f)
print(result)
