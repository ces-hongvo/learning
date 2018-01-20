x = [3, 6, 5, 4, 9, 8, 1, 0, 2, 7]
n = len(x)
y = [3, 6, 5, 4, 9, 8, 1, 0, 2, 7]

def merge(x,y,a,b,c):
    p = a
    i = a
    j = b+1
    while(i <= b and j <= c):
        if(x[i] <= x[j]):
            y[p] = x[i]
            i += 1
        else:
            y[p] = x[j]
            j += 1
        p += 1
    if(i <= b):
        for h in range(i,b+1):
            y[p] = x[h]
            p += 1
    if(j <= c):
        for h in range(j,c+1):
            y[p] = x[h]
            p += 1

def mergeByLength(x,y,parLen,sumLen):
    a = 0
    b = parLen - 1
    c = b + parLen
    while c <= sumLen:
        merge(x,y,a,b,c)
        a = a + (2*parLen)
        b = b + (2*parLen)
        c = c + (2*parLen)
    if(b <= sumLen):
        merge(x,y,a,b,sumLen)
    else:
        if(a <= sumLen):
            for h in range(a, sumLen+1):
                y[h] = x[h]

flag = True
parLen = 1
while(parLen < n):
    if(flag):
        mergeByLength(x,y,parLen,n-1)
    else:
        mergeByLength(y,x,parLen,n-1)
    parLen = parLen * 2
    flag = not flag
if(flag):
    print(x)
else:
    print(y)