x = [5, 1, 4, 2, 3, 6, 8, 7]
n = len(x)
for i in range(1, n):
    tmp = x[i]
    j = i-1
    while(x[j]>tmp and j>-1):
        x[j+1]=x[j]
        j = j-1
    x[j+1] = tmp
print(x)