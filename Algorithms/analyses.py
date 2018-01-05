def tryIt(i, n, x, t):
    root = 1
    lastSum = 0
    if (i > 0):
        root = x[i-1]
        lastSum = t[i-1]
    for j in range(root, n+1-root):
        x[i] = j
        t[i] = lastSum + x[i]
        if (x[i] + lastSum == n):
            print(x)
        elif (x[i] + lastSum < n):
            tryIt(i+1, n, x, t)
        else:
            x[i] = 0
            t[i] = 0
            break


x = []
t = []
n = 6
i = 0
for num in range(n):
    x.append(0)
    t.append(0)
tryIt(i, n, x, t)
