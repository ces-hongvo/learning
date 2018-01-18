x = [[0,0,1], [0,1,1], [1,1,1], [1,1,0], [1,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
n = len(x)
m = len(x[0])
print(x)
def exchangeSort(l,h,x,k,m):
    i = l
    j = h
    if(k>m-1):
        return
    while(i < j):
        while(x[j][k] == 1):
            j -= 1
        while(x[i][k] == 0):
            i += 1
        if(i < j):
            for id in range(m):
                tmp = x[i][id]
                x[i][id] = x[j][id]
                x[j][id] = tmp
    if(i==j):
        i -= 1
    if(i>j):
        i-=1
        j+=1
    exchangeSort(l,i,x,k+1,m)
    exchangeSort(j,h,x,k+1,m)

exchangeSort(0,n-1,x,0,m)
print(x)
