x = [5, 1, 4, 2, 3, 6, 8, 7]
jmin = 0
n = len(x)
for i in range(n):
    jmin = i
    for j in range(i+1, n):
        if (x[j] < x[jmin]):
            jmin = j
    if(i != jmin):
        tmp = x[i]
        x[i] = x[jmin]
        x[jmin] = tmp

print(x)
