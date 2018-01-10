x = [5, 1, 4, 2, 3, 6, 8, 7]
n = len(x)
for i in range(1,n):
    for j in range(n-1,i-1,-1):
        if x[j] < x[j-1]:
            tmp = x[j]
            x[j] = x[j-1]
            x[j-1] = tmp
print(x)
