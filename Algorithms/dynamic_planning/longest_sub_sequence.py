a = [-100,5,2,3,4,9,10,5,6,7,8,100]
n = len(a)
l = []
t = []
for i in range(n):
    t.append(0)
    l.append(0)

def optimize(l,t,n):
    l[n-1] = 1
    for i in range(n-2,-1,-1):
        jmax = n-1
        for j in range(i+1,n-1):
            if(a[i]<a[j] and l[j]>l[jmax]):
                jmax = j
        l[i] = l[jmax] + 1
        t[i] = jmax

optimize(l,t,n)
print(l)
print(t)
result = []
seqLen = l[0]
result.append(a[0])
for i in range(1,n):
    if(l[i] == seqLen - 1):
        result.append(a[i])
        seqLen = seqLen - 1
print(result)