x = []
n = 5
k = 3
for num in range(k):
    x.append(num+1)

print(x)
i = k-1
while(True):
    i = k-1
    while(i>=0 and x[i]==n-k+i+1):
        i -= 1;
    if(i>=0):
        x[i] = x[i] + 1
        for j in range(i+1,k):
            x[j] = x[j-1] + 1;
        print(x)
    else:
        break
