def tryIt (i, n, k, x, c):
    for num in range(n):
        if(c[num]):
            x[i] = num+1
            if (i==k-1):
                print(x)
            else:
                c[num] = False
                tryIt(i+1, n, k, x, c)
                c[num] = True
x = []
c = []
n = 5
k = 3
for j in range(n):
    c.append(True)
for j in range(k):
    x.append(0)
tryIt(0,n,k,x,c)     