x = []
n = 4
for num in range(4):
    x.append(num+1)
print(x)
while(True):
    i = n-1
    while (x[i-1] > x[i]):
        i -= 1
    i = i - 1
    if(i >= 0):
        k = n - 1
        while (x[k] < x[i]):
            k -= 1
        tmp = x[i]
        x[i] = x[k]
        x[k] = tmp
        a = i+1
        b = n-1
        while(a < b):
            tmp0 = x[a]
            x[a] = x[b]
            x[b] = tmp0
            a += 1
            b -= 1
        print(x)
    else:
        break
