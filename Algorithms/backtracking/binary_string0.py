def tryIt (i, n, x):
    for j in range(2):
        x[i] = j
        if i == n-1:
            print(x)
        else:
            tryIt(i+1, n, x)

x = []
n = 3
for i in range(n):
    x.append(0)
tryIt(0, n, x)
