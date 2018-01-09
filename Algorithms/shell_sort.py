x = [5, 1, 4, 2, 3, 6, 8, 7]
n = len(x)
h = (int)(n/2)
while(h > 0):
    for i in range(h, n):
        tmp = x[i]
        j = i-h
        while(j >= 0 and x[j] > tmp):
            x[j+h] = x[j]
            j = j - h
        j = j + h
        x[j] = tmp
    h = (int)(h / 2)
print(x)
    