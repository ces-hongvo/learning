x = [5, 1, 4, 2, 3, 6, 8, 7]
n = len(x)
for j in range(1,n):
    tmp = x[j]
    inf = 0
    sup = j-1
    while(inf <= sup):
        median = (int)((inf + sup) / 2)
        if (tmp > x[median]):
            inf = median + 1
        elif (tmp < x[median]):
            sup = median - 1
    for k in range(j, inf, -1):
        x[k] = x[k-1]
    x[inf] = tmp
print(x)