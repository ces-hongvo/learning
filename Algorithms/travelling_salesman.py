def tryIt(i, C, max, n, x, t, free, minSpending):
    for j in range(1,n-1):
        if (free[j]):
            x[i] = j
            t[i] = t[i-1] + C[x[i-1]][j]
            if(t[i] < minSpending[0]):
                if (i < n-2):
                    free[j] = False
                    tryIt(i+1, C, max, n, x, t, free, minSpending)
                    free[j] = True
                else:
                    if (t[n-2] + C[x[n-2]][0]) < minSpending[0]:
                        print(x)
                        minSpending[0] = t[n-2] + C[x[n-2]][0]
                    x = []
                    t = []
                    free = []
                    for num in range(n):
                        x.append(0)
                        t.append(0)
                        free.append(True)
                    free[0] = False
                    break



C = [[0, 3, 2, 1], [3, 0, 1, 2],
     [2, 1, 0, 4], [1, 2, 4, 0]]
max = 200
n = 5
x = []
t = []
free = []
for num in range(n):
    x.append(0)
    t.append(0)
    free.append(True)
free[0] = False
minSpending = [max]
tryIt(1, C, max, n, x, t, free, minSpending)
