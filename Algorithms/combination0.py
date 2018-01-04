def tryIt(i , n, k, x):
    root = 1
    if (i > 0):
        root = x[i-1]
    for num in range(root+1, n+1):
        x[i] = num
        if (i == k-1):
            print(x)
        else:
            tryIt(i+1, n, k, x)
x = []
n = 5
k = 3
for j in range(k):
    x.append(j+1)

tryIt(1, n, k, x)
