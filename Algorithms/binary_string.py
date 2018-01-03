x = []
n = 5
for i in range(n):
    x.append(0)

print(x)
i = n-1
while (True):
    i = n-1;
    while (i >= 0 and x[i] == 1): 
        i = i - 1

    if (i>=0):
        x[i] = 1
        for j in range(i+1, n):
            x[j] = 0
        print(x)
    else :
        break
