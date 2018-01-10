def tryIt(i, n, k, x, a, b, c, count):
    for j in range(n):
        if(a[j] and b[i-j+n-1] and c[i+j]):
            x[i] = j
            a[j] = False
            b[i-j+n-1] = False
            c[i+j] = False
            if(i == k-1):
                print(x)
                count[0] = count[0] + 1
                a[j] = True
                b[i-j+n-1] = True
                c[i+j] = True
            elif(i < k-1):
                tryIt(i+1, n, k, x, a, b, c, count)
                a[j] = True
                b[i-j+n-1] = True
                c[i+j] = True

n = 8
k = 8
x = []
a = []
b = []
c = []
count = [0]
for num in range(n):
    x.append(0)
    a.append(True)
for num0 in range((n*2)):
    b.append(True)
    c.append(True)
tryIt(0, n, k, x, a, b, c, count)
print(count)
