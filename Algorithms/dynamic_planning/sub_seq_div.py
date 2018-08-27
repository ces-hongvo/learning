from __future__ import print_function
a = [1, 6, 11, 5, 10, 15, 20, 2, 4, 9]
n = len(a)
k = 5
f = []
infinite = n+10
for i in range(n+1):
    tmp = []
    for j in range(k):
        tmp.append(0)
    f.append(tmp)
f[0][0] = 0
for i in range(1,k):
    f[0][i] = infinite

def subOnMod(subedNum, modNum):
    tmp = subedNum % modNum
    return tmp

def optimize(a, n, k, f):
    for i in range(1, n + 1):
        for j in range(k):
            tmpMin = f[i-1][j]
            if(f[i-1][j] > 1 + f[i-1][subOnMod(j-a[i-1], k)]):
                tmpMin = 1 + f[i-1][subOnMod(j-a[i-1], k)]
            f[i][j] = tmpMin

def trace(a, n, k, f):
    s = sum(a)
    result = []
    mod = s % k
    while(mod > 0):
        min = f[0][mod]
        indexa = 0
        for i in range(1, n+1):
            if f[i][mod] < min:
                min = f[i][mod]
                indexa = i
        if min != f[0][mod]:
            result.insert(0, a[indexa-1])
            s = s-a[indexa-1]
            mod = s % k
    return result


optimize(a, n, k, f)
result = trace(a, n, k, f)
for i in range(n+1):
    for j in range(k):
        print(f[i][j], end="\t")
    print("")
print(result)
