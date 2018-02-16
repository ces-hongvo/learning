import math
a = [-100,5,2,3,4,9,10,5,6,7,8,100]
n = len(a)
l = []
t = []
startOf = []
for i in range(n):
    t.append(0)
    l.append(0)
    startOf.append(0)
startOf[1] = n-1
m = 1

def findInSO(i, a, startOf, m):
    inf = 1
    sup = m+1
    while(inf + 1 < sup):
        median = math.floor((inf + sup)/2)
        j = startOf[median]
        if a[j] > a[i]:
            inf = median
        else:
            sup = median
    return startOf[inf]

def optimize(a, l, t, n, m, startOf):
    l[n-1] = 1
    for i in range(n-2,-1,-1):
        j = findInSO(i, a, startOf, m)
        k = l[j]+1
        if(k > m):
            m = k
            startOf[k] = i
        else:
            if a[i] > a[startOf[k]]:
                startOf[k] = i
        l[i]=k
        t[i]=j



optimize(a,l,t,n,m, startOf)
print("a", a)
print("l", l)
print("t", t)
print("startOf", startOf)
result = []
seqLen = l[0]
result.append(a[0])
for i in range(1,n):
    if(l[i] == seqLen - 1):
        result.append(a[i])
        seqLen = seqLen - 1
print("result", result)
