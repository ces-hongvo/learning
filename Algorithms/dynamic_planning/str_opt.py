x = 'abcdqqq'
y = 'eabdft'
m = len(x)
n = len(y)
f = []
for i in range(m+1):
    tmp = []
    for j in range(n+1):
        tmp.append(0)
    f.append(tmp)
for i in range(m+1):
    f[i][0] = i
for j in range(n+1):
    f[0][j] = j

def optimize(x, y, m, n, f):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if(x[i-1] == y[j-1]):
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = min(f[i-1][j-1], f[i][j-1], f[i-1][j]) + 1
    return

def trace(x, y, m, n, f):
    i = m
    j = n
    result = []
    while(i != 0 or j != 0):
        if(x[i-1] == y[j-1]):
            i = i-1
            j = j-1
        else:
            if(f[i][j] == f[i-1][j-1] + 1):
                result.insert(0, "replace " + x[i-1] + " by " + y[j-1])
                i = i-1
                j = j-1
            elif(f[i][j] == f[i-1][j] + 1):
                result.insert(0, "x delete " + x[i-1])
                i = i-1
            elif(f[i][j] == f[i][j-1] + 1):
                result.insert(0, "x append " + y[j-1])
                j = j-1
    return result

optimize(x, y, m, n, f)
result = trace(x, y, m, n, f)
for i in range(m+1):
    for j in range(n+1):
        print(f[i][j], end="\t")
    print("")
print(result)
