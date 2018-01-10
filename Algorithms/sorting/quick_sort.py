x = [5, 1, 4, 2, 3, 6, 8, 7]
n = len(x)
def partitionSort(l, h, x):
    if (l >= h):
        return
    elif (h-l == 1):
        if(x[l] > x[h]):
            temp = x[l]
            x[l] = x[h]
            x[h] = temp
        return
    pivot = (int)((l+h)/2)
    i = l
    j = h
    while(i < j):
        while(x[i] < x[pivot]):
            i = i + 1
        while(x[j] > x[pivot]):
            j = j - 1
        if(i < j):
            tmp = x[i]
            x[i] = x[j]
            x[j] = tmp
    partitionSort(j, h, x)
    partitionSort(l, i, x)

partitionSort(0, n-1, x)
print(x)
